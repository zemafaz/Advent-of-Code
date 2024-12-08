package year2024;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.logging.Logger;

public class Day01HistorianHysteria {

    static PriorityQueue<Integer> left = new PriorityQueue<Integer>();
    static PriorityQueue<Integer> right = new PriorityQueue<Integer>();
    static HashMap<Integer, Counter> counter = new HashMap<Integer, Counter>();

    public static int part1(FileReader inputFile) throws IOException {
        while (inputFile.ready()) {
            part1ParseFile(inputFile);
        }

        Logger.getGlobal().fine(String.format("Left size: %d", left.size()));
        Logger.getGlobal().fine(String.format("Right size: %d", right.size()));

        Integer res = 0;
        while (!left.isEmpty()) {
            res += Math.abs(left.poll() - right.poll());
        }
        return res;
    }

    private static void part1ParseFile(FileReader inputFile) throws NumberFormatException, IOException {
        BufferedReader input = new BufferedReader(inputFile);
        String line;
        while ((line = input.readLine()) != null) {
            Integer firstSpace = line.indexOf(' ');
            Integer number = Integer.parseInt(line.substring(0, firstSpace));
            left.add(number);
            number = Integer.parseInt(line.substring(firstSpace).stripLeading());
            right.add(number);
        }
    }

    public static int part2(FileReader inputFile) throws IOException {
        Day01HistorianHysteria outer = new Day01HistorianHysteria();
        BufferedReader input = new BufferedReader(inputFile);
        String line;
        while ((line = input.readLine()) != null) {
            Integer firstSpace = line.indexOf(' ');
            Integer number = Integer.parseInt(line.substring(0, firstSpace));
            if (counter.get(number) == null) {
                counter.put(number, outer.new Counter(1, 0));
            } else {
                counter.get(number).left++;
            }
            number = Integer.parseInt(line.substring(firstSpace).stripLeading());
            if (counter.get(number) == null) {
                counter.put(number, outer.new Counter(0, 1));
            } else {
                counter.get(number).right++;
            }
        }

        int res = 0;
        for (Map.Entry<Integer, Counter> entry: counter.entrySet()) {
            res += entry.getKey() * entry.getValue().calculateTimes();
        }

        return res;
    }

    private class Counter {
        public int left;
        public int right;

        public Counter(int left, int right) {
            this.left = left;
            this.right = right;
        }

        public int calculateTimes() {
            return this.left * this.right;
        }

        @Override
        public String toString() {
            return String.format("{left: %d, right: %d}", this.left, this.right);
        }
    }

}

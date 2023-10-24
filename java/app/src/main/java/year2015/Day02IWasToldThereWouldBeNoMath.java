package year2015;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.PriorityQueue;
import java.util.Scanner;

class Day02IWasToldThereWouldBeNoMath {

    public static int part1(Scanner scanner) {
        int res = 0;
        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().split("x");
            int extra = Integer.MAX_VALUE;
            for (int i=0; i<line.length; i++) {
                int side = Integer.parseInt(line[i%(line.length)]) * Integer.parseInt(line[(i+1)%line.length]); 
                res += (2 * side);
                extra = Integer.min(side, extra);
            }
            res += extra;
        }
        
        return res;
    }

    public static int part2(Scanner scanner) {
        int res = 0;
        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().split("x");
            PriorityQueue<Integer> sides = new PriorityQueue<Integer>(line.length);
            int extra = 1;
            for (int i=0; i<line.length; i++) {
                int side = Integer.parseInt(line[i]);
                sides.add(side);
                extra *= side;
            }
            res += 2 * sides.poll() + 2 * sides.poll() + extra;
        }
        
        return res;
    }

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("src/main/resources/201502_input");
        if (!file.exists()) {
            throw new FileNotFoundException();
        }
        Scanner scanner = new Scanner(file);
        int res = 0;
        switch (args[0]) {
            case "part1":
                res = part1(scanner);
                break;
            case "part2":
                res = part2(scanner);
                break;
            default:
                break;
        }
        scanner.close();
        System.out.printf("Result: %d%n", res);
    }
}

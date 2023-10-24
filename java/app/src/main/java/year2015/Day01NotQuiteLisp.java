package year2015;

import java.io.FileReader;
import java.io.IOException;

public class Day01NotQuiteLisp {
    
    public static int part1(FileReader input) throws IOException {
        int res = 0;
        while (input.ready()) {
            final char character = (char) input.read();
            switch (character) {
                case '(':
                    res++;
                    break;
                case ')':
                    res--;
                    break;
                default:
                    break;
            }
        }
        
        return res;
    }

    public static int part2(FileReader input) throws IOException {
        int res = 0;
        int i = 1;
        while (input.ready()) {
            final char character = (char) input.read();
            switch (character) {
                case '(':
                    res++;
                    break;
                case ')':
                    res--;
                    break;
                default:
                    break;
            }
            if (res == -1) {
                return i;
            }
            i++;
        }
        
        return -1;
    }

}

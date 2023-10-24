package year2015;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.io.FileReader;
import java.io.IOException;

class Day01NotQuiteLispTest {

    @Test
    void testPart1() throws IOException {
        final FileReader input = new FileReader("src/main/resources/201501_input");
        final int expected_solution = 280;
        final int res = Day01NotQuiteLisp.part1(input);
        assertEquals(res, expected_solution);
    }

    @Test
    void testPart2() throws IOException {
        final FileReader input = new FileReader("src/main/resources/201501_input");
        final int expected_solution = 1797;
        final int res = Day01NotQuiteLisp.part2(input);
        assertEquals(res, expected_solution);
    }
}

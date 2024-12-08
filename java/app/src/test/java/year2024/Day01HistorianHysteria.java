package year2024;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Disabled;
import static org.junit.jupiter.api.Assertions.*;

import java.io.FileReader;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

class Day01HistorianHysteriaTest {

    @Disabled
    @Test
    void testPart1() throws IOException {
        Logger.getGlobal().setLevel(Level.ALL);

        final FileReader input = new FileReader("src/test/resources/202401_input");
        final int expectedSolution = 11;
        final int res = Day01HistorianHysteria.part1(input);
        assertEquals(expectedSolution, res);
    }

    @Test
    void testPart2() throws IOException {
        final FileReader input = new FileReader("src/test/resources/202401_input");
        final int expected_solution = 31;
        final int res = Day01HistorianHysteria.part2(input);
        assertEquals(expected_solution, res);
    }
}

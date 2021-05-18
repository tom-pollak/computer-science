import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.Random;

import org.junit.Test;

public class TestQuestion_2_iii {

    @Test(timeout = 5000)
    /**
     * Test if the dynamic programming approach works correctly and efficiently
     * on a feasible level.
     * The test should take less than 0.5 seconds to complete. A timeout has 
     * been set to 5 seconds to ensure that for a large level, an inefficient
     * implementation would fail.
     */
	public void testFeasible() {		
        // Series of tests to ensure that the outcome on small level is
        // correct.
        assertTrue(LevelChecker.betterCheck(new int[]{1,1,1,1,1}));
        assertTrue(LevelChecker.betterCheck(new int[]{1,2,0,1,2}));
        assertTrue(LevelChecker.betterCheck(new int[]{3,1,2,0,4,0,1}));
        assertTrue(LevelChecker.betterCheck(new int[]{4,0,0,0,1}));
        assertTrue(LevelChecker.betterCheck(new int[]{5,3,2,1,0,1}));

        // Generating a large feasible level of 63 springboards.
        int[] base = new int[]{5,4,3,2,1,1};
        int repetition = 10;
        int[] level = new int[repetition * base.length + 3];
        for (int i = 0; i < repetition; i++) {
           for (int j = 0; j < base.length; j++) {
                level[i * base.length + j + 1] = base[j];
            }
        }
        level[0] = level.length - 1;
        level[level.length - 2] = 0;
        level[level.length - 1] = 1;

        // This level should be resolved in less than a second using 
        // a dynamic programming strategy. A brute force implementation
        // would take more than a minute and therefore fail the test.
        assertTrue(LevelChecker.betterCheck(level));
	}

    @Test(timeout = 5000)
    /**
     * Test if the dynamic programming approach works correctly and efficiently
     * on a NON solvable level.
     * The test should take less than 0.5 seconds to complete. A timeout has 
     * been set to 5 seconds to ensure that for a large level, an inefficient
     * implementation would fail.
     */
	public void testNotFeasible() {
        // Series of tests to ensure that the outcome on small level is
        // correct.
        assertFalse(LevelChecker.betterCheck(new int[]{0,1,1,1,1}));
        assertFalse(LevelChecker.betterCheck(new int[]{2,0,3,0}));
        assertFalse(LevelChecker.betterCheck(new int[]{3,2,1,0,2,1,2}));
        assertFalse(LevelChecker.betterCheck(new int[]{2,3,0,2,1,0,2}));
        assertFalse(LevelChecker.betterCheck(new int[]{2,3,0,2,1,1,0}));

        // Generating a large non-solvable level of 60 springboards.
        int[] base = new int[]{4,3,2,1,0,1};
        int[] level = new int[60];
        Random rd = new Random();
        for (int i = 0; i < level.length - base.length; i++) {
            level[i] = rd.nextInt(5)+1;
        }
        for (int j = 0; j < base.length; j++) {
            level[level.length - base.length + j] = base[j];
        }

        // This level should be resolved in less than a second using 
        // a dynamic programming strategy. A brute force implementation
        // would take more than a minute and therefore fail the test.
        assertFalse(LevelChecker.betterCheck(level));
	}

}

import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Test;

public class TestQuestion_2_ii {

    @Test
    /**
     * Test if getJumps returns the minimum list of jumps needed to solve the level.
     */
	public void testFeasible() {		
        assertEquals(Arrays.asList(1,1,1,1), LevelChecker.getJumps(new int[]{1,1,1,1,1}));
        assertEquals(Arrays.asList(4), LevelChecker.getJumps(new int[]{4,0,0,0,1}));
        assertEquals(Arrays.asList(3,3,1), LevelChecker.getJumps(new int[]{3,1,1,3,1,0,1,2}));
        assertEquals(Arrays.asList(2,2,2), LevelChecker.getJumps(new int[]{3,1,2,0,4,0,1}));
	}

    @Test
    /**
     * Test if the method getJumps returns an empty list if the level is not 
     * solvable.
     */
	public void testNotFeasible() {		
        assertEquals(new ArrayList<Integer>(), LevelChecker.getJumps(new int[]{0,1,1,1,1}));
        assertEquals(new ArrayList<Integer>(), LevelChecker.getJumps(new int[]{2,0,3,0}));
        assertEquals(new ArrayList<Integer>(), LevelChecker.getJumps(new int[]{3,2,1,0,2,0,2}));
        assertEquals(new ArrayList<Integer>(), LevelChecker.getJumps(new int[]{3,2,1,0,2,0,2}));
        assertEquals(new ArrayList<Integer>(), LevelChecker.getJumps(new int[]{2,3,0,2,1,1,0}));
	}


}

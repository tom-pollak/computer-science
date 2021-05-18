import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class TestQuestion_2_i {

    @Test
    /**
     * Test if the method check returns true if the level is feasible.
     */
	public void testFeasible() {		
        assertTrue(LevelChecker.check(new int[]{1,1,1,1,1}));
        assertTrue(LevelChecker.check(new int[]{1,2,0,1,2}));
        assertTrue(LevelChecker.check(new int[]{3,1,2,0,4,0,1}));
        assertTrue(LevelChecker.check(new int[]{4,0,0,0,1}));
	}

    @Test
    /**
     * Test if the method check returns false if the level is not feasible.
     */
	public void testNotFeasible() {		
        assertFalse(LevelChecker.check(new int[]{0,1,1,1,1}));
        assertFalse(LevelChecker.check(new int[]{2,0,3,0}));
        assertFalse(LevelChecker.check(new int[]{3,2,1,0,2,0,2}));
        assertFalse(LevelChecker.check(new int[]{2,3,0,2,1,0,2}));
        assertFalse(LevelChecker.check(new int[]{2,3,0,2,1,1,0}));
	}

}

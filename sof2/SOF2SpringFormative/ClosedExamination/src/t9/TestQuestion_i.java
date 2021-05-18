package t9;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class TestQuestion_i {

	T9Pad pad;

	/**
	 * [15 marks] Test if we can retrieve characters associated to a numeric key.
	 */
	@Test
	public void testGetKeyCode() {
		pad = new T9Pad();
		pad.addKey(2, "abc");
		pad.addKey(3, "def");
		Integer expected = 2;
		assertEquals(expected, pad.getKeyCode('a'));
		assertEquals(expected, pad.getKeyCode('b'));
		assertEquals(expected, pad.getKeyCode('c'));
		expected = 3;
		assertEquals(expected, pad.getKeyCode('d'));
		assertEquals(expected, pad.getKeyCode('e'));
		assertEquals(expected, pad.getKeyCode('f'));
	}

	/**
	 * [10 marks] Test if we trying to retrieve the key of a non existent characters
	 * throws an exception.
	 */
	@Test(expected = IllegalArgumentException.class)
	public void testGetKeyCodeError() {
		pad = new T9Pad();
		pad.addKey(2, "abc");
		pad.addKey(3, "def");
            pad.getKeyCode('z');
	}

}

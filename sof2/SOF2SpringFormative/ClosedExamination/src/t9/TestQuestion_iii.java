package t9;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import org.junit.Test;

public class TestQuestion_iii {

	T9Pad pad;

	/**
	 * [15 marks] Test if two words are textonyms.
	 */
	@Test
	public void testWord2T9() {
		pad = new T9Pad();
		pad.addKey(2, "abc");
		pad.addKey(3, "def");
		pad.addKey(4, "ghi");
		pad.addKey(5, "jkl");
		pad.addKey(6, "mno");
		pad.addKey(7, "pqrs");
		pad.addKey(8, "tuv");
		pad.addKey(9, "wxyz");

		assertTrue(pad.isTextonym("good", "home"));
		assertTrue(pad.isTextonym("hood", "home"));
		assertTrue(pad.isTextonym("good", "hood"));
	}

	/**
	 * [10 marks] Test if two words are not textonyms.
	 */
	@Test
	public void testWord2T9False() {
		pad = new T9Pad();
		pad.addKey(2, "abc");
		pad.addKey(3, "def");
		pad.addKey(4, "ghi");
		pad.addKey(5, "jkl");
		pad.addKey(6, "mno");
		pad.addKey(7, "pqrs");
		pad.addKey(8, "tuv");
		pad.addKey(9, "wxyz");

		assertFalse(pad.isTextonym("good", "hoods"));
		assertFalse(pad.isTextonym("good", "hogs"));
	}
}

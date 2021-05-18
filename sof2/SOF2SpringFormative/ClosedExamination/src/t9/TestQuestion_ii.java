package t9;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;
import org.junit.Test;

public class TestQuestion_ii {
	T9Pad pad;

	/**
	 * [17 marks] Test if we can retrieve all characters from a numeric pad. Note
	 * the pad may be incomplete.
	 */
	@Test
	public void testGetPadLetters() {
		pad = new T9Pad();
		pad.addKey(2, "abc");
		pad.addKey(3, "def");
		pad.addKey(4, "ghi");
		pad.addKey(5, "jkl");
		pad.addKey(6, "mno");
		pad.addKey(7, "pqrs");
		pad.addKey(8, "tuv");

		// Test a partially completed numeric pad
		Character[] letters = new Character[] { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
				'o', 'p', 'q', 'r', 's', 't', 'u', 'v' };
		assertTrue(pad.getPadLetters().containsAll(Arrays.asList(letters)));
		assertTrue(Arrays.asList(letters).containsAll(pad.getPadLetters()));
		assertEquals(Arrays.asList(letters).size(), pad.getPadLetters().size());

		// test a fully completed numeric pad
		pad.addKey(9, "wxyz");
		letters = new Character[] { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
				'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
		assertTrue(pad.getPadLetters().containsAll(Arrays.asList(letters)));
		assertTrue(Arrays.asList(letters).containsAll(pad.getPadLetters()));
		assertEquals(Arrays.asList(letters).size(), pad.getPadLetters().size());
	}

	/**
	 * [8 marks] Test if we can retrieve all characters from a numeric pad. Note
	 * the pad may be incomplete.
	 */
	@Test
	public void testGetPadLettersEmpty() {
		pad = new T9Pad();
		assertTrue((pad.getPadLetters()).isEmpty());
	}

}

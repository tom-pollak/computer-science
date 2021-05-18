package t9;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import org.junit.Before;
import org.junit.Test;

public class TestQuestion_v {

	// Known Mapping of larger dictionary <t9code,word> to compare our result
	// against
	Map<String, String> mappingT9;

	// T9Tree built using the large dictionary from mappingT9.
	T9Tree tree;

	/**
	 * Setup method to build our tree and mapping before each test.
	 * 
	 * @throws Exception
	 */
	@Before
	public void setUp() throws Exception {
		// The mapping stored as a string
		String mapping = "in, 46\n a, 2\n publication, 78254228466\n of, 63\n new, 639\n scientist, 724368478\n you, 968\n could, 26853\n randomise, 726366473\n all, 255\n the, 843\n letters, 5388377\n keeping, 5337464\n the, 843\n first, 34778\n two, 896\n and, 263\n last, 5278\n two, 896\n the, 843\n same, 7263\n and, 263\n readability, 73232245489\n would, 96853\n hardly, 427359\n be, 23\n affected, 23332833\n my, 69\n analysis, 26259747\n did, 343\n not, 668\n come, 2663\n to, 86\n much, 6824\n because, 2322873\n the, 843\n theory, 843679\n at, 28\n the, 843\n time, 8463\n was, 927\n for, 367\n shape, 74273\n and, 263\n sequence, 73783623\n recognition, 73264648466\n saberi, 722374\n work, 9675\n suggests, 78443787\n we, 93\n may, 629\n have, 4283\n some, 7663\n powerful, 76937385\n parallel, 72725535\n processors, 7762377677\n at, 28\n work, 9675\n the, 843\n reason, 732766\n for, 367\n this, 8447\n is, 47\n surely, 787359\n that, 8428\n identifying, 43368439464\n content, 2668368\n by, 29\n parallel, 72725535\n processing, 7762377464\n speeds, 773337\n up, 87\n recognition, 73264648466\n we, 93\n only, 6659\n need, 6333\n the, 843\n first, 34778\n and, 263\n last, 5278\n two, 896\n letters, 5388377\n to, 86\n spot, 7768\n changes, 2426437\n in, 46\n meaning, 6326464\n";
		Scanner input = new Scanner(mapping);
		mappingT9 = new HashMap<>();

		// parsing the string to build the mapping between words and t9code
		while (input.hasNextLine()) {
			String line = input.nextLine();
			String[] items = line.split(",");
			mappingT9.put(items[0].trim(), items[1].trim());
		}
		input.close();

		// building the tree based on the mapping done above
		tree = new T9Tree();
		for (String word : mappingT9.keySet()) {
			tree.add(mappingT9.get(word), word);
		}
	}

	/**
	 * [7 marks] test the method getAllWords(String t9code). The first series of
	 * test is on a small dictionary of 7 words used in the question description. It
	 * is here to help you debug your code if it doesn't work. The second part of
	 * the test is on a larger dictionary which is much harder to track bugs from.
	 */
	@Test
	public void testGetAllWordsString() {
		// build the tree with a 7 words dictionary
		T9Tree smallTree = new T9Tree();
		smallTree.add("4663", "good");
		smallTree.add("4663", "home");
		smallTree.add("4663", "hood");
		smallTree.add("4663", "hoof");
		smallTree.add("46637", "goods");
		smallTree.add("46637", "homes");
		smallTree.add("46637", "hoods");

		// build the expected result
		Set<String> words = new HashSet<>();

		// three words have the prefix 46637, so had them to the expected
		// result.
		words.add("goods");
		words.add("homes");
		words.add("hoods");
		assertEquals(words, smallTree.getAllWords("46637"));

		// four more words have the prefix 4663, so add them to the expected
		// result. Including the one with prefix 46637, the expected result adds
		// up to 7 words, i.e the entire smallTree dictionary. Therefore any
		// sub-prefix of 4663 should return the full dictionary.
		words.add("good");
		words.add("home");
		words.add("hood");
		words.add("hoof");
		assertEquals(words, smallTree.getAllWords("4663"));
		// test that any prefix of 4663 returns the entire smallTree dictionary.
		assertEquals(words, smallTree.getAllWords("466"));
		assertEquals(words, smallTree.getAllWords("46"));
		assertEquals(words, smallTree.getAllWords("4"));
		assertEquals(words, smallTree.getAllWords(""));

		// Testing on a larger dictionary
		words = new HashSet<>();
		words.add("you");
		words.add("would");
		assertEquals(words, tree.getAllWords("968"));
		words.add("work");
		assertEquals(words, tree.getAllWords("96"));

		// Some words have a prefix starting with 2, so should not return an
		// empty set.
		assertNotEquals(new HashSet<>(), tree.getAllWords("2"));
	}

	/**
	 * [2 marks] test the method getAllWords(String t9code). Test if the method
	 * returns and empty set when no words exist with the given prefix.
	 */
	@Test
	public void testGetAllWordsStringEmpty() {
		// build the tree with a 7 words dictionary
		T9Tree smallTree = new T9Tree();
		smallTree.add("4663", "good");
		smallTree.add("4663", "home");
		smallTree.add("4663", "hood");
		smallTree.add("4663", "hoof");
		smallTree.add("46637", "goods");
		smallTree.add("46637", "homes");
		smallTree.add("46637", "hoods");

		// build the expected result
		Set<String> words = new HashSet<>();

		// no word in the dictionary has the prefix 466373, so the expected
		// result is an empty set
		assertEquals(words, smallTree.getAllWords("466373"));
		// no word in the dictionary has the prefix 4623, so the expected
		// result is an empty set
		assertEquals(words, smallTree.getAllWords("4623"));

		// no words have a prefix starting with 1 or 0 as no characters
		// associated with these two digits. Therefore should return an empty
		// Set.
		assertEquals(new HashSet<>(), tree.getAllWords("1"));
		assertEquals(new HashSet<>(), tree.getAllWords("0"));

	}

	/**
	 * [1 marks] Test the method getAllWords(String t9code) throws an exception if
	 * the t9code contains keys that are not part of the numeric pad.
	 */
	@Test(expected = IllegalArgumentException.class)
	public void testGetAllWordsStringError() {
		// build the tree with a 7 words dictionary
		T9Tree smallTree = new T9Tree();
		smallTree.add("4663", "good");
		smallTree.add("4663", "home");
		smallTree.add("4663", "hood");
		smallTree.add("4663", "hoof");
		smallTree.add("46637", "goods");
		smallTree.add("46637", "homes");
		smallTree.add("46637", "hoods");

		// invalid key for our keypad.
        smallTree.getAllWords("a");
	}
}

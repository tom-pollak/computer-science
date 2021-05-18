package t9;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map.Entry;
import java.util.Set;

public class T9Pad {

  /**
   * keep the mapping between numeric key and alphabet characters. The keys of the map are integer
   * comprised between 0..9 included, the values are set of lower case alphabet characters.
   */
  HashMap<Integer, Set<Character>> pad;

  /**
   * Construct an empty keypad. Numeric key and mapped characters must be added via the method
   * addKey(Integer, String).
   */
  public T9Pad() {
    pad = new HashMap<Integer, Set<Character>>();
  }

  /**
   * Adds to the pad the mapping between key and every characters in the String letters.
   *
   * <p>For example, addKey(2, "abc") should add the mappings (2, 'a'), (2, 'b'), and (2, 'c') to
   * the pad.
   *
   * @param key
   * @param letters
   * @throws IllegalArgumentException if any of the arguments is null, or if the key is not
   *     comprised between 0 and 9 included.
   */
  public void addKey(Integer key, String letters) {
    // Sanity check of all parameters
    if (letters == null || key == null || key < 0 || key > 9) {
      throw new IllegalArgumentException();
    }

    Set<Character> currentLetters = pad.get(key);
    if (currentLetters == null) {
      currentLetters = new HashSet<>();
    }
    for (int i = 0; i < letters.length(); i++) {
      currentLetters.add(letters.charAt(i));
    }
    pad.put(key, currentLetters);
  }

  @Override
  public String toString() {
    String output = "<T9Pad:\n";
    for (Integer key : pad.keySet()) {
      output += key + ":";
      for (Character letter : pad.get(key)) {
        output += letter;
      }
      output += "\n";
    }
    output += ">";
    return output;
  }

  /**
   * Returns the set of keys used in the keypad, that is all the digits that are paired with at
   * least one character
   *
   * @return the set of keys used on the keypad
   */
  public Set<Integer> keySet() {
    return pad.keySet();
  }

  public Integer getKeyCode(Character letter) {
    Set<Entry<Integer, Set<Character>>> characterSet = pad.entrySet();
    for (Entry<Integer, Set<Character>> entry : characterSet) {
      if (entry.getValue().contains(letter)) {
        return entry.getKey();
      }
    }
    throw new IllegalArgumentException("No mapping for letter: " + letter);
  }

  public List<Character> getPadLetters() {
    Set<Character> set = new HashSet<Character>();
    Set<Entry<Integer, Set<Character>>> characterSet = pad.entrySet();
    for (Entry<Integer, Set<Character>> entry : characterSet) {
      set.addAll(entry.getValue());
    }
    List<Character> alphabet = new ArrayList<Character>();
    alphabet.addAll(set);
    return alphabet;
  }

  public boolean isTextonym(String word1, String word2) {
    if (word1.length() != word2.length()) {
      return false;
    }
    for (int i = 0; i < word1.length(); i++) {
      try {
        if (getKeyCode(word1.charAt(i)) != getKeyCode(word2.charAt(i))) {
          return false;
        }
      } catch (IllegalArgumentException e) {
        return false;
      }
    }
    return true;
  }

  public static void main(String[] args) {
    T9Pad a = new T9Pad();
    a.addKey(1, "abc");
    a.addKey(2, "def");
    System.out.println(a.keySet());
    System.out.println(a.getKeyCode('a'));
    System.out.println(a.getPadLetters());
    System.out.println(a.isTextonym("afb", "cez"));
  }
}

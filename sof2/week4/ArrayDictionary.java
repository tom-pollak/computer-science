public class ArrayDictionary {
	private Integer[] keys;
	private String[] values;

	public int indexOf(Integer key) {
		for (int i = 0; i < keys.length; i++) {
			if (keys[i] == key) {
				return i;
			}
		}
		return -1;
	}

	public int size() {
		int count = 0;
		for (int i = 0; i < keys.length; i++) {
			if (keys[i] != null) {
				count++;
			}
		}
		return count;
	}

	public ArrayDictionary() {
		keys = new Integer[100];
		values = new String[100];
	}

	public ArrayDictionary(int size) {
		keys = new Integer[size];
		values = new String[size];
	}

	public String toString() {
		String output = "{ ";
		for (int i = 0; i < keys.length; i++) {
			if (values[i] != null) {
				output += keys[i] + ": " + values[i] + ", ";
			}
		}
		output += "}";
		return output;
	}

	public String put(Integer key, String value) {
		int index = indexOf(key);
		if (index == -1) {
			if (keys.length == size()) {
				Integer[] newKeys = new Integer[keys.length * 2];
				String[] newValues = new String[keys.length * 2];
				System.arraycopy(keys, 0, newKeys, 0, keys.length);
				System.arraycopy(values, 0, newValues, 0, values.length);
				keys = newKeys;
				values = newValues;
			}
			int nullIndex = indexOf(null);
			keys[nullIndex] = key;
			values[nullIndex] = value;
			return null;
		}
		String oldValue = values[index];
		values[index] = value;
		return oldValue;
	}

	public boolean contains(Integer key) {
		int index = indexOf(key);
		if (index == -1) {
			return false;
		}
		return true;
	}

	public String get(Integer key) {
		int index = indexOf(key);
		if (index == -1) {
			return null;
		}
		return values[index];
	}

	public boolean isEmpty() {
		if (size() == 0) {
			return true;
		}
		return false;
	}

	public static void main(String[] args) {
		ArrayDictionary dict = new ArrayDictionary(4);
		for (int i = 0; i < 10000; i++) {
			dict.put(i, Integer.toString(i));
		}
		System.out.println(dict);
	}
}

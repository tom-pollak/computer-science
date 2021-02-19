package Tally;

public class TallyCounter {
	private int counter;

	public TallyCounter() {
		counter = 0;
	}

	@Override
	public String toString() {
		String format = String.format("%0%d", 3 - String.valueOf(counter).length());
		return String.format(format, counter);
	}
}

import java.util.Scanner;

public class TrainingZone {
	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		System.out.print("Enter age ");
		int age = keyboard.nextInt();
		double m = 208 - 0.7 * age;

		System.out.print("Enter heart rate ");
		int rate = keyboard.nextInt();

		if (rate >= 0.9 *m) {
			System.out.println("Interval training");
		} else if (rate >= 0.7 * m) {
			System.out.println("Threshold training");
		} else if (rate >= 0.5 * m) {
			System.out.println("Aerobic training");
		} else {
			System.out.println("Couch potato");
		}
		keyboard.close();
	}
}

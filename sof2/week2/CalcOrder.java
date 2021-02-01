import java.util.Scanner;

public class CalcOrder {
	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		System.out.print("Enter no of kilos of bananas");
		float bananasKilos = keyboard.nextFloat();
		keyboard.close();

		float total = bananasKilos * 3 + 4.99f;
		if (total > 50) {
			total -= 3.49;
		}
		System.out.println("Total cost:" + total);
	}
}

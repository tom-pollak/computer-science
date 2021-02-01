import java.util.Scanner;

public class SumInt {
    public static void main(String[] args) {
        int number = 1;
        int total = 0;
        Scanner keyboard = new Scanner(System.in);
        while (number != 0) {
            System.out.print("enter an integer: ");
            number = keyboard.nextInt();
            total += number;
        }
        System.out.println("Total: " + total);
    }
}
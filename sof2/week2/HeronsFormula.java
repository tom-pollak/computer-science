import java.util.Scanner;

public class HeronsFormula {
    private static final String LENGTH_STRING = "Enter side length: ";
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.print(LENGTH_STRING);
        int a = keyboard.nextInt();
        System.out.print(LENGTH_STRING);
        int b = keyboard.nextInt();
        System.out.print(LENGTH_STRING);
        int c = keyboard.nextInt();
        keyboard.close();
        double s = (a + b + c) / 2;
        double A = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        System.out.println("Area: " + A);
    }
}

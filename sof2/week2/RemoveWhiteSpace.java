import java.util.Scanner;

public class RemoveWhiteSpace {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String sentence = keyboard.nextLine().toLowerCase();
        String noSpaceSentence = sentence.replaceAll("\\s", "");
        System.out.println(noSpaceSentence);
        String camelSentence = "";
        int i = 0;
        while (i < sentence.length()) {
            char c = sentence.charAt(i);
            if (c == ' ') {
                i++;
                camelSentence = camelSentence + sentence.substring(i, i+1).toUpperCase();
            } else {
                camelSentence = camelSentence + sentence.substring(i, i + 1);
            }
            i++;
        }
        System.out.println(camelSentence);

    }
}
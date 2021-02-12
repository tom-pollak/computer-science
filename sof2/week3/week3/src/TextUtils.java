import java.util.ArrayList;

public class TextUtils {
    public static ArrayList<String> split(String text, String seperators) {
        ArrayList<String> splitString = new ArrayList<String>();
        String subString = "";
        for (int i=0;i < text.length(); i++) {
            if (seperators.indexOf(text.charAt(i)) == -1) {
                subString = subString + text.charAt(i);
            } else {
                splitString.add(subString);
                subString = "";
            }
        }
        splitString.add(subString);
        return splitString;
    }
    public static void main(String[] args) {
        String sentence = "the dog!jumped@over&the moon";
        String seperators = "!@#$%^&*( ";
        System.out.println(sentence + " --> " + TextUtils.split(sentence, seperators));
    }
}

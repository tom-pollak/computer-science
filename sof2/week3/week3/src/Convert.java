public class Convert {
    public static double toBase10(String binary) {
        double total = 0;
        for (int i = (binary.length()-1); i >= 0; i--) {
            total = total + Math.pow(2, i) * Character.getNumericValue(binary.charAt(i));
        }
        return total;
    }
    public static void main(String[] args) throws Exception {
        String binary = "11111111";
        System.out.println(binary + " --> " + Convert.toBase10(binary));
        binary = "00000000";
        System.out.println(binary + " --> " + Convert.toBase10(binary));
        binary = "10001011";
        System.out.println(binary + " --> " + Convert.toBase10(binary));
    }
}

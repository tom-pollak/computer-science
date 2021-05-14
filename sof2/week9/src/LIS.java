import java.util.Arrays;

public class LIS {
    public static int[] getSlice(int[] array, int startIndex, int endIndex) {
        if (startIndex >= endIndex) {
            int[] emptyArr = new int[0];
            return emptyArr;
        }

        int[] slicedArray = new int[endIndex - startIndex];
        for (int i=0; i < slicedArray.length; i++) {
            slicedArray[i] = array[startIndex + i];
        }
        return slicedArray;
    }

    public static int getLIS(int[] sequence, int count) {
        int newCount = 0;
        count += 1;
        if (sequence.length == 1) {
            return count;
        }
        int[] newSequence = getSlice(sequence, 1, sequence.length);
        if (sequence[0] < sequence[1]) {
            newCount = getLIS(newSequence, count);
        }
        else {
            newCount = getLIS(newSequence, 0);
        }

        if (newCount > count) {
            count = newCount;
        }
        return count;
    }
    

    public static void main(String[] args) {
        int[] sequence = {1, 3 ,5, 9, 5, 6, 1, 3, 5, 6, 10, 12, 3};
        int LIS = getLIS(sequence, 0);
        System.out.println(Arrays.toString(sequence) + ": " + String.valueOf(LIS));
    }
}

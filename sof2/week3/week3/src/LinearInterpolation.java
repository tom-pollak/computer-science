public class LinearInterpolation {
	public static int[][] resample(int[] data) {
		int[] sample = new int[2 * (data.length - 1) + 1];
		for (int i = 0; i < data.length; i++) {
			sample[2 * i] = data[i];
		}
		for (int i = 1; i < sample.length - 1; i+= 2) {
			for (int j = 0; j < scale; j++) {
				sample[i + j] = (int) Math.round((sample[i] * (scale - j)
												+ sample[i + scale] * j)
												/ (double) scale);
			}
		}
		return sample;
	}	
}

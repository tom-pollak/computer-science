public class Hamiltonian {
    public static boolean arrayContainsInt(int[] array, int number) {
        for (int i : array) {
            if (number == i) {
                return true;
            }
        }
        return false;
    }

    public static boolean isHamiliontian(int[][] adjacencyMatrix) {
        int currentState = 0;
        boolean[] usedState = new boolean[adjacencyMatrix.length];
        usedState[0] = true;
        for (int i = 1; i < adjacencyMatrix.length; i++) {
            if (usedState[i] == false) {
                usedState[i] = true;
                if (adjacencyMatrix[currentState][i] == 1 && adjacencyMatrix[i][currentState] == 1) {
                    
                } else if (adjacencyMatrix[currentState][i] == 0 && adjacencyMatrix[i][currentState] == 0) {

                }
                
            }
            
        }
    }
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
    }
}

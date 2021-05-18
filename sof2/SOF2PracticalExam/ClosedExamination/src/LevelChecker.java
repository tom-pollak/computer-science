import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class LevelChecker {
  public static boolean check(int[] level) {
    if (level.length == 1 && level[0] > 0) {
      return true;
    }
    if (level[0] == 0) {
      return false;
    }

    int maxJump = Math.min(level[0], level.length - 1);
    for (int i = 1; i <= maxJump; i++) {
      int[] A = Arrays.copyOfRange(level, i, level.length);
      if (check(A)) {
        return true;
      }
    }
    return false;
  }

  public static List<Integer> getJumps(int[] level) {
    List<Integer> sequence = new ArrayList<Integer>();
    if (level.length == 1 && level[0] > 0) {
      sequence.add(0);
      return sequence;
    }
    if (level[0] == 0) {
      return sequence;
    }

    int maxJump = Math.min(level[0], level.length - 1);
    for (int i = 1; i <= maxJump; i++) {
      int[] A = Arrays.copyOfRange(level, i, level.length);
      List<Integer> newSequence = getJumps(A);
      // If new sequence is shorter than old best sequence
      if ((newSequence.size() < sequence.size() || sequence.isEmpty()) && !newSequence.isEmpty()) {
        // Don't want finish node in sequence
        if (newSequence.get(0) == 0) {
          newSequence.clear();
        }
        sequence = newSequence;
        // Add next jump to start of sequence
        sequence.add(0, i);
      }
    }
    System.out.println(sequence);
    return sequence;
  }

  public static boolean betterCheck(int[] level) {
    boolean[] steps = new boolean[level.length];
    LinkedList<Integer> stepQueue = new LinkedList<Integer>();
    LinkedList<Integer> positionQueue = new LinkedList<Integer>();
    stepQueue.add(level[0]);
    positionQueue.add(0);
    while (stepQueue.size() != 0) {
      int position = positionQueue.poll();
      int step = stepQueue.poll();
      if (position == level.length - 1) {
        return true;
      }

      steps[position] = true;
      int maxStep = Math.min(position + step, level.length - 1);

      for (int i = position + 1; i <= maxStep; i++) {
        if (!steps[i] && level[i] != 0) {
          positionQueue.add(i);
          stepQueue.add(level[i]);
        }
      }
    }
    return false;
  }
}

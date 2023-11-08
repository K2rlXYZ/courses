package collections.set;

import org.junit.Test;

import java.util.*;


public class Birthday {

    @Test
    public void runCode() {

        Random r = new Random();


        List<Integer> vals = new ArrayList<>();

        for (int x = 0; x < 1000; x++) {
            int randomDayOfYear = r.nextInt(365);
            int randomDayOfYear2 = r.nextInt(365);
            int iter = 0;
            while (true) {
                randomDayOfYear2 = r.nextInt(365);
                if (randomDayOfYear == randomDayOfYear2) {
                    vals.add(iter);
                    break;
                }
                iter++;
            }
        }
        System.out.println(vals);
        double sum = 0.0;
        for (Integer i : vals) {
            sum += 1.0 / i;
        }
        sum = sum / vals.size();
        sum *= 100;
        System.out.println(sum);
        // pick random day in a loop
        // find how many iterations till first collision (got the same number)


    }

}

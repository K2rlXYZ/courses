package collections.benchmark;

import oo.hide.Timer;
import org.junit.Test;

import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;


public class Runner {

    @Test
    public void benchmarkDifferentImplementations() {

        Set<Integer> set1 = new MySet();
        Set<Integer> set2 = new TreeSet<>();
        Set<Integer> set3 = new HashSet<>();

        Timer timer = new Timer();

        for (int x = 0; x < 30000; x++){
            set3.add(2);
        }

        System.out.println(timer.getPassedTime());
    }

}

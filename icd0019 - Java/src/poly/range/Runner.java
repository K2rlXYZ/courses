package poly.range;

import org.junit.Test;

import java.util.Arrays;
import java.util.Iterator;
import java.util.stream.IntStream;

public class Runner {

    @Test
    public void canIterateRange() {
        for (Integer integer : range(1, 7)) {
            System.out.println(integer);
        }
    }

    private Iterable<Integer> range(int start, int end) {
        Iterable<Integer> iter = new Iterable<Integer>() {
            @Override
            public Iterator<Integer> iterator() {
                return Arrays.stream(IntStream.range(start, end).toArray()).iterator();
            }
        };
        return iter;
    }


}

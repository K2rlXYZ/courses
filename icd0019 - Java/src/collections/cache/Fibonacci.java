package collections.cache;

import java.util.ArrayList;
import java.util.List;

public class Fibonacci {

    List<Entry> cache = new ArrayList<>();

    public Integer fib(Integer n) {
        if (n < 1) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        if (cache.stream().anyMatch(i -> i.fib_n == n)) {
            for (Entry e : cache) {
                if (e.fib_n == n) {
                    return e.fib_val;
                }
            }
        }
        int calc = fib(n - 1) + fib(n - 2);
        cache.add(new Entry(n, calc));
        return calc;
    }

}

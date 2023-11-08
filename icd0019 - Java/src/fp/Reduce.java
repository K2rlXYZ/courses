package fp;

import inheritance.constructor.Bird;
import org.junit.Test;

import java.util.List;
import java.util.function.BiFunction;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.is;

public class Reduce {

    @Test
    public void reducesListToSingleResult() {

        var numbers = List.of(1, 2, 3, 4);

        assertThat(reduce(numbers, (a, b) -> a + b), is(10));

        assertThat(reduce(numbers, (a, b) -> a * b), is(24));

        assertThat(reduce(List.of("1", "2", "3"), (a, b) -> a + b), is("123"));

    }

    private <T> T reduce(List<T> list, BiFunction<T, T, T> func) {
        T val = list.get(0);
        for (int x = 1; x < list.size(); x++) {
            val = func.apply(val, list.get(x));
        }
        return val;
    }
}

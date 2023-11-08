package generics.pair;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;

public class Runner {

    @Test
    public void pairExample() {
        Pair<String, Integer> pair = new Pair<>("key", 1);

        String key = pair.getFirst();
        Integer value = pair.getSecond();

        assertThat(key, is("key"));
        assertThat(value, is(1));
    }
}

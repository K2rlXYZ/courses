package exceptions.validate;

import org.junit.Test;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.is;

public class MinimumElementTests {

    @Test
    public void findsMinimumFromArrayOfNumbers() {

        assertThat(MinimumElement.minimumElement(new int[]{1, 3}), is(1));

        assertThat(MinimumElement.minimumElement(new int[]{1, 0}), is(0));
    }

    @Test
    public void emptyArray() {
        try {
            MinimumElement.minimumElement(new int[]{});
        } catch (Exception e) {
            assertThat(e.getClass(), equalTo(IllegalArgumentException.class));
        }

        try {
            MinimumElement.minimumElement(null);
        } catch (Exception e) {
            assertThat(e.getClass(), equalTo(IllegalArgumentException.class));
        }
    }

}

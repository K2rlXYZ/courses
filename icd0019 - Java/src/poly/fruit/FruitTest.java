package poly.fruit;

import org.junit.Test;

import java.util.Arrays;
import java.util.List;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;

public class FruitTest {

    @Test
    public void computesTotalWeight() {


        List<Weighable> fruits = Arrays.asList(new Apple(0.1), new Orange(120));

        assertThat(getTotalWeightInGrams(fruits), is(220));
    }

    private int getTotalWeightInGrams(List<Weighable> list) {
        return list.stream().map(Weighable::getWeightInGrams).mapToInt(i -> i).sum();
    }

}

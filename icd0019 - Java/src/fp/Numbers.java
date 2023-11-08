package fp;

import org.junit.Test;

import java.util.Arrays;
import java.util.List;

public class Numbers {

    private List<Integer> numbers = Arrays.asList(1, 3, 4, 51, 24, 5);

    @Test
    public void findsOddNumbers() {

        List<Integer> oddNumbers = numbers.stream().filter(i -> i % 2 == 1).toList();

        System.out.println(oddNumbers);
    }

    @Test
    public void findsOddNumbersOver10() {

        List<Integer> oddNumbersOverTen = numbers.stream().filter(i -> i % 2 == 1 && i > 10).toList();

        System.out.println(oddNumbersOverTen);

    }

    @Test
    public void findsSquaredOddNumbers() {
        List<Integer> oddNumbersSquares = numbers.stream().filter(i -> i % 2 == 1).map(i -> i * i).toList();

        System.out.println(oddNumbersSquares);
    }

    @Test
    public void findsSumOfOddNumbers() {
        int oddNumbersSummed = numbers.stream().filter(i -> i % 2 == 1).reduce(0, Integer::sum);

        System.out.println(oddNumbersSummed);
    }

}

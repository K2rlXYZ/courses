package junit;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.*;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.Assert.*;

@SuppressWarnings("PMD")
public class Tests {

    @Test
    public void equalityExamples() {
        assertTrue(1 == 1);
        assertFalse(1 == 2);

        Integer x2 = 1;
        Integer y2 = 1;
        assertTrue(x2 == y2);

        Integer x = 128;
        Integer y = 128;
        assertFalse(x == y);
        assertTrue(x.equals(y));
        assertTrue("abc" == "abc");
        assertTrue("abc" == "a" + "bc");

        String a = "a";
        assertFalse("abc" == a + "bc");
        assertTrue("abc".equals(a + "bc"));
    }

    @Test
    public void assertThatAndAssertEqualsExample() {
        assertThat(1 + 2, is(3));
        assertThat(1 + 2, is(not(4)));
        assertThat(new int[]{1, 2, 3}, is(new int[]{1, 2, 3}));
        assertThat(new int[]{1, 2, 3}, is(not(new int[]{1, 2})));
    }

    @Test
    public void findsSpecialNumbers() {
        assertTrue(Code.isSpecial(0));
        assertTrue(Code.isSpecial(1));
        assertTrue(Code.isSpecial(2));
        assertTrue(Code.isSpecial(3));
        assertTrue(Code.isSpecial(11));
        assertTrue(Code.isSpecial(36));

        assertFalse(Code.isSpecial(4));
        assertFalse(Code.isSpecial(15));
        assertFalse(Code.isSpecial(37));

    }

    @Test
    public void findsLongestStreak() {
        assertThat(Code.longestStreak(""), is(0));

        assertThat(Code.longestStreak("a"), is(1));

        assertThat(Code.longestStreak("abbcccaaaad"), is(4));
    }


    @Test
    public void findsModeFromCharactersInString() {
        assertThat(Code.mode(null), is(nullValue()));

        assertThat(Code.mode(""), is(nullValue()));
        assertThat(Code.mode("abcb"), is('b'));
        assertThat(Code.mode("cbbc"), is('c'));

        assertThat(Code.getCharacterCount("abcb", 'b'), is(2));
        assertThat(Code.getCharacterCount("abcbb", 'b'), is(3));
        assertThat(Code.getCharacterCount("abcb", 'c'), is(1));
    }

    @Test
    public void removesDuplicates() {
        assertThat(Code.removeDuplicates(arrayOf(1, 1)), is(arrayOf(1)));

        assertThat(Code.removeDuplicates(arrayOf(1, 2, 1, 3, 2)), is(arrayOf(1, 2, 3)));

        assertThat(Code.removeDuplicates(arrayOf(1, 2, 3)), is(arrayOf(1, 2, 3)));

        assertThat(Code.removeDuplicates(arrayOf(100, 0, 3, 100, 0, 4, 562, 4)),
                is(arrayOf(100, 0, 3, 4, 562)));
    }

    @Test
    public void sumsIgnoringDuplicates() {
        assertThat(Code.sumIgnoringDuplicates(arrayOf(1, 1)), is(1));

        assertThat(Code.sumIgnoringDuplicates(arrayOf(1, 2, 1, 3, 2)), is(6));

        assertThat(Code.sumIgnoringDuplicates(arrayOf(1, 2, 3)), is(6));
    }

    private int[] arrayOf(int... numbers) {
        return numbers;
    }

}

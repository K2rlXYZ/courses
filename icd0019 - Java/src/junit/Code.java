package junit;

import java.util.*;

public class Code {

    public static boolean isSpecial(int candidate) {
        int div = candidate % 11;
        return div == 0 || div == 1 || div == 2 || div == 3;
    }

    public static int longestStreak(String inputString) {
        if (Objects.equals(inputString, "")) {
            return 0;
        }
        StringBuilder streak = new StringBuilder();
        java.util.Map<Character, Integer> dict = new LinkedHashMap<>();
        for (int x = 0; x < inputString.length(); x++) {
            if (streak.length() != 0 && inputString.charAt(x) == streak.charAt(0)) {
                streak.append(inputString.charAt(x));
            } else {
                if (streak.length() != 0) {
                    dict.put(streak.charAt(0), streak.length());
                }
                streak = new StringBuilder();
                streak.append(inputString.charAt(x));
            }
        }
        if (streak.length() != 0) {
            dict.put(streak.charAt(0), streak.length());
        }
        return Collections.max(dict.entrySet(), Comparator.comparingInt(Map.Entry::getValue)).getValue();
    }

    public static Character mode(String input) {
        if (Objects.equals(input, "") || input == null) {
            return null;
        }
        java.util.Map<Character, Integer> dict = new LinkedHashMap<>();
        for (int x = 0; x < input.length(); x++) {
            if (dict.containsKey(input.charAt(x))) {
                continue;
            }
            dict.put(input.charAt(x), getCharacterCount(input, input.charAt(x)));
        }
        return Collections.max(dict.entrySet(), Comparator.comparingInt(Map.Entry::getValue)).getKey();
    }

    public static int getCharacterCount(String allCharacters, char targetCharacter) {
        int count = 0;
        for (int x = 0; x < allCharacters.length(); x++) {
            if (allCharacters.charAt(x) == targetCharacter) {
                count += 1;
            }
        }
        return count;
    }

    public static int[] removeDuplicates(int[] integers) {
        int ind = 0;
        Integer[] temp = new Integer[integers.length];
        for (int i : integers) {
            boolean noneMatch = true;
            for (Integer j : temp) {
                if (j == null) {
                    break;
                }
                if (j == i) {
                    noneMatch = false;
                }
            }
            if (noneMatch) {
                temp[ind] = i;
                ind += 1;
            }
        }
        int[] fin = new int[ind];
        for (int x = 0; x < fin.length; x++) {
            fin[x] = temp[x];
        }
        return fin;
    }

    public static int sumIgnoringDuplicates(int[] integers) {
        int[] withoutDuplicates = removeDuplicates(integers);
        int sum = 0;
        for (int i : withoutDuplicates) {
            sum += i;
        }
        return sum;
    }


}

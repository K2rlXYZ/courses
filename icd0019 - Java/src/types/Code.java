package types;

import java.util.*;

public class Code {

    public static void main(String[] args) {

        int[] numbers = {1, 3, -2, 9};

        System.out.println(mode("abcb"));

        System.out.println(sum(numbers));
        System.out.println(squareDigits("2"));
        System.out.println(squareDigits("a2b"));
        System.out.println(squareDigits("b2a8"));
        System.out.println(squareDigits("2"));

        System.out.println(isolatedSquareCount());
    }

    public static int sum(int[] numbers) {
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        return sum;
    }

    public static double average(int[] numbers) {
        return Double.valueOf(sum(numbers)) / numbers.length;
    }

    public static Integer minimumElement(int[] integers) {
        if (Arrays.equals(integers, new int[]{})) {
            return null;
        }
        int smallest = integers[0];
        for (int integer : integers) {
            if (smallest > integer) {
                smallest = integer;
            }
        }
        return smallest;
    }

    public static String asString(int[] elements) {
        if (elements.length == 0) {
            return "";
        }
        StringBuilder str = new StringBuilder(String.valueOf(elements[0]));
        for (int x = 1; x < elements.length; x++) {
            str.append(", ").append(String.valueOf(elements[x]));
        }
        return str.toString();
    }

    public static Character mode(String input) {
        if (input == ""){
            return null;
        }
        java.util.Map<Character, Integer> dict = new HashMap<>();
        for (int x = 0; x < input.length(); x++) {
            if (dict.containsKey(input.charAt(x))) {
                dict.put(input.charAt(x), dict.get(input.charAt(x)) + 1);
            } else {
                dict.put(input.charAt(x), 1);
            }
        }
        return Collections.max(dict.entrySet(), Comparator.comparingInt(Map.Entry::getValue)).getKey();
    }

    public static String squareDigits(String s) {
        StringBuilder newstr = new StringBuilder();
        for (int x = 0; x < s.length(); x++) {
            if (Character.isDigit(s.charAt(x))) {
                newstr.append(String.valueOf((int) Math.pow(Character.digit(s.charAt(x), 10), 2)));
            } else {
                newstr.append(s.charAt(x));
            }
        }
        return newstr.toString();
    }

    public static int isolatedSquareCount() {
        boolean[][] matrix = getSampleMatrix();

        printMatrix(matrix);


        int isolatedCount = 0;

        // count isolates squares here

        for (int rowIndex = 0; rowIndex < matrix.length; rowIndex++) {
            for (int elementIndex = 0; elementIndex < matrix[rowIndex].length; elementIndex++) {
                if (checkTopRow(matrix, rowIndex, elementIndex) &&
                        checkMiddleRow(matrix, rowIndex, elementIndex) &&
                        checkBottomRow(matrix, rowIndex, elementIndex)) {
                    isolatedCount += 1;
                }
            }
        }

        return isolatedCount;
    }

    private static boolean checkTopRow(boolean[][] matrix, int rowIndex, int elementIndex) {
        return !(isValidIndex(matrix, rowIndex + 1, elementIndex - 1) &&
                getValueFromArray(matrix, rowIndex + 1, elementIndex - 1)) &&

                !(isValidIndex(matrix, rowIndex + 1, elementIndex) &&
                        getValueFromArray(matrix, rowIndex + 1, elementIndex));
    }

    private static boolean checkMiddleRow(boolean[][] matrix, int rowIndex, int elementIndex) {
        return !(isValidIndex(matrix, rowIndex, elementIndex - 1) &&
                getValueFromArray(matrix, rowIndex, elementIndex - 1)) &&

                !(isValidIndex(matrix, rowIndex, elementIndex + 1) &&
                        getValueFromArray(matrix, rowIndex, elementIndex + 1)) &&

                !(isValidIndex(matrix, rowIndex - 1, elementIndex - 1) &&
                        getValueFromArray(matrix, rowIndex - 1, elementIndex - 1));
    }

    private static boolean checkBottomRow(boolean[][] matrix, int rowIndex, int elementIndex) {
        return !(isValidIndex(matrix, rowIndex + 1, elementIndex + 1) &&
                getValueFromArray(matrix, rowIndex + 1, elementIndex + 1)) &&

                !(isValidIndex(matrix, rowIndex - 1, elementIndex) &&
                        getValueFromArray(matrix, rowIndex - 1, elementIndex)) &&

                !(isValidIndex(matrix, rowIndex - 1, elementIndex + 1) &&
                        getValueFromArray(matrix, rowIndex - 1, elementIndex + 1));
    }

    private static void printMatrix(boolean[][] matrix) {
        for (boolean[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }

    private static boolean[][] getSampleMatrix() {
        boolean[][] matrix = new boolean[10][10];

        Random r = new Random(5);
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                matrix[i][j] = r.nextInt(5) < 2;
            }
        }

        return matrix;
    }

    public static boolean isValidIndex(boolean[][] arr, int x, int y) {
        return x >= 0 && y >= 0 && y < arr.length && x < arr[y].length;
    }

    public static boolean getValueFromArray(boolean[][] arr, int x, int y) {
        return arr[y][x];
    }
}

package intro;

import static java.lang.Math.floor;

public class Program {

    public static void main(String[] args) {

        int decimal = asDecimal("11001101");

        System.out.println(decimal); // 205

        String binary = asString(205);

        System.out.println(binary);
    }

    public static String asString(int input) {
        StringBuilder str = new StringBuilder();
        while (input != 0) {
            if (input % 2 == 0) {
                str.append("0");
                input = input / 2;
            } else {
                str.append("1");
                input = (int) floor(input / 2);
            }
        }
        return str.reverse().toString();
    }

    public static int asDecimal(String input) {
        int sum = 0;
        input = new StringBuilder(input).reverse().toString();
        for (int x = 0; x < input.length(); x++) {
            if (input.charAt(x) == '1') {
                sum += pow(2, x);
            }
        }
        return sum;
    }

    private static int pow(int arg, int power) {
        // Java has Math.pow() but this time write your own implementation.
        if (power == 0) {
            return 1;
        }

        int sum = arg;
        for (int x = 1; x < power; x++) {
            sum *= arg;
        }
        return sum;
    }
}

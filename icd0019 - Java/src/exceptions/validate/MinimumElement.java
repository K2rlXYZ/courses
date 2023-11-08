package exceptions.validate;

public class MinimumElement {

    public static Integer minimumElement(int[] integers) {
        try {
            int minimumElement = integers[0];

            for (int current : integers) {
                if (current < minimumElement) {
                    minimumElement = current;
                }
            }

            return minimumElement;
        } catch (Exception exception) {
            throw new IllegalArgumentException();
        }
    }

}

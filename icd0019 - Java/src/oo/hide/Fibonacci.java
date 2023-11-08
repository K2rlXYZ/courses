package oo.hide;

public class Fibonacci {
    public int[] fibSequence = {};

    public int[] addToIntArray(int[] arr, int num) {
        int[] temp = new int[arr.length + 1];
        for (int x = 0; x < arr.length; x++) {
            temp[x] = arr[x];
        }
        temp[temp.length - 1] = num;
        return temp;
    }

    public int nextValue() {
        switch (fibSequence.length) {
            case 0:
                fibSequence = addToIntArray(fibSequence, 0);
                break;
            case 1:
                fibSequence = addToIntArray(fibSequence, 1);
                break;
            default:
                fibSequence = addToIntArray(fibSequence, fibSequence[fibSequence.length - 1] + fibSequence[fibSequence.length - 2]);
                break;
        }
        return fibSequence[fibSequence.length - 1];
    }

}

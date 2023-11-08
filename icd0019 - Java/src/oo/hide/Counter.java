package oo.hide;

public class Counter {
    private int start, step;

    public Counter(int inStart, int inStep) {
        start = inStart-inStep;
        step = inStep;
    }

    public int nextValue() {
        start += step;
        return start;
    }
}

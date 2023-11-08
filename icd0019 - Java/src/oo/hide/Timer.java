package oo.hide;

import static java.lang.Math.round;

public class Timer {
    long start;
    public Timer() {
        start = System.currentTimeMillis();
    }

    public String getPassedTime() {
        return String.format("%s sek", (double)(System.currentTimeMillis()-start)/1000);
    }
}

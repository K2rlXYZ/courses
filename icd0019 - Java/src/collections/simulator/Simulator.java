package collections.simulator;

import java.util.*;

public class Simulator {

    @SuppressWarnings("PMD.UnusedPrivateField")
    private double iterations;

    public Simulator(double iterations) {
        this.iterations = iterations;
    }

    public Map<HandType, Double> calculateProbabilities() {
        throw new RuntimeException("not implemented yet");
    }

    public double getWinningOdds(Hand player1hand, Hand player2hand) {
        throw new RuntimeException("not implemented yet");
    }

}

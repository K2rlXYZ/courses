package poly.undo;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Calculator {

    private double value;
    private List<HashMap<Boolean, Double>> operations = new ArrayList<>();

    public void input(double value) {
        this.value = value;
        HashMap<Boolean, Double> op = new HashMap();
        op.put(null, value);
        operations.add(op);
    }

    public void add(double addend) {
        value += addend;
        HashMap<Boolean, Double> op = new HashMap();
        op.put(false, addend);
        operations.add(op);
    }

    public void multiply(double multiplier) {
        value *= multiplier;
        HashMap<Boolean, Double> op = new HashMap();
        op.put(true, multiplier);
        operations.add(op);
    }

    public double getResult() {
        return value;
    }

    public void undo() {
        HashMap<Boolean, Double> op = operations.get(operations.size() - 1);
        if (op.containsKey(null)) {
            this.value = 0;
        } else if (op.containsKey(true)) {
            this.value /= op.get(true);
        } else {
            this.value -= op.get(false);
        }
        operations.remove(operations.size() - 1);
    }
}

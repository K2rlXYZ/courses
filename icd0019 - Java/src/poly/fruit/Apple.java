package poly.fruit;

public class Apple implements Weighable {

    private Double weightInKiloGrams;

    public Apple(Double weight) {
        this.weightInKiloGrams = weight;
    }

    @Override
    public Integer getWeightInGrams() {
        return (int) (weightInKiloGrams * 1000);
    }
}


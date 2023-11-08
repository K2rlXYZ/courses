package generics.list;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> {

    private List<T> elements = new ArrayList<>();

    public void add(T element) {
        elements.add(element);
    }

    public void addAll(List<? extends Number> elementsf) {
        for (Number element : elementsf) {
            elements.add((T) element);
        }
    }

    @Override
    public String toString() {
        return elements.toString();
    }
}

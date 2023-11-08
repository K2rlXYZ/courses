package generics.cart;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Objects;

public class ShoppingCart<T extends CartItem> {

    double lastDiscount = 0;
    double currentDiscount = 100;
    private List<T> cart = new ArrayList<>();

    public void add(T item) {
        cart.add(item);
    }

    public void removeById(String id) {
        T temp = null;
        for (T item : cart) {
            if (Objects.equals(item.getId(), id)) {
                temp = item;
            }
        }
        cart.remove(temp);
    }

    public Double getTotal() {
        double total = 0;
        for (T item : cart) {
            total += item.getPrice() * currentDiscount / 100;
        }
        return total;
    }

    public void increaseQuantity(String id) {
        T temp = null;
        for (T item : cart) {
            if (item.getId().equals(id)) {
                temp = item;
            }
        }
        cart.add(temp);
    }

    public void applyDiscountPercentage(Double discount) {
        lastDiscount = currentDiscount;
        currentDiscount = currentDiscount - (currentDiscount * discount / 100);
    }

    public void removeLastDiscount() {
        currentDiscount = lastDiscount;
    }

    public void addAll(List<T> items) {
        for (T item: items) {
            cart.add(item);
        }
    }

    @Override
    public String toString() {
        StringBuilder retstr = new StringBuilder();
        HashMap<String, Integer> counts = new HashMap<>();
        for (T item : cart) {
            if (counts.containsKey(item.getId())) {
                counts.put(item.getId(), counts.get(item.getId()) + 1);
            } else {
                counts.put(item.getId(), 1);
            }
        }
        List<String> completed = new ArrayList<>();
        for (T item : cart) {
            if (!completed.contains(item.getId())) {
                retstr.append("(").append(item.getId()).append(", ").append(item.getPrice()).append(", ").append(counts.get(item.getId())).append("), ");
                completed.add(item.getId());
            }
        }
        String finstr = retstr.toString();
        return finstr.substring(0, finstr.length() - 2);
    }
}

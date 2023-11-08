package fp.sales;

import java.io.FileNotFoundException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class Analyser {

    private Repository repository;

    public Analyser(Repository repository) {
        this.repository = repository;
    }

    public Double getTotalSales() {
        return repository.getEntries().stream().mapToDouble(Entry::getAmount).sum();
    }

    public Double getSalesByCategory(String category) {
        return repository.getEntries().stream().filter(i -> i.getCategory().equals(category)).mapToDouble(Entry::getAmount).sum();
    }

    public Double getSalesBetween(LocalDate start, LocalDate end) {
        return repository.getEntries().stream().filter(i -> i.getDate().compareTo(start) > 0).filter(i -> i.getDate().compareTo(end) < 0).mapToDouble(Entry::getAmount).sum();
    }

    public String mostExpensiveItems() {
        String endStr = Arrays.toString(repository.getEntries().stream().sorted(Comparator.comparingDouble(Entry::getAmount).reversed()).limit(3).map(Entry::getProductId).sorted().toArray());
        return endStr.substring(1, endStr.length() - 1);
    }

    public String statesWithBiggestSales() {
        HashMap<String, Double> states = new HashMap<>();
        repository.getEntries().forEach(entry -> {
            if (states.containsKey(entry.getState())) {
                states.put(entry.getState(), states.get(entry.getState()) + entry.getAmount());
            } else {
                states.put(entry.getState(), entry.getAmount());
            }
        });
        String endStr = Arrays.toString(states.entrySet().stream().sorted((e1, e2) -> Double.compare(e2.getValue(), e1.getValue())).limit(3).map(Map.Entry::getKey).toArray());
        return endStr.substring(1, endStr.length()-1);
    }
}

package inheritance.analyser;

import java.util.*;

public sealed abstract class SalesAnalyser permits DifferentiatedTaxSalesAnalyser, FlatTaxSalesAnalyser, TaxFreeSalesAnalyser {

    public List<SalesRecord> salesRecords;

    public SalesAnalyser(List<SalesRecord> records) {
        salesRecords = records;
    }

    protected abstract Double getTotalSales();

    protected Double getTotalSalesByProductId(String id) {
        double totalSales = 0;
        for (SalesRecord rc : salesRecords) {
            if (rc.getProductId().equals(id)) {
                totalSales += rc.getItemsSold() * rc.getProductPrice();
            }
        }
        return totalSales;
    }

    protected String getIdOfMostPopularItem() {
        HashMap<String, Integer> rebuild = new LinkedHashMap<>();
        for (SalesRecord rc : salesRecords) {
            if (rebuild.containsKey(rc.getProductId())) {
                rebuild.put(rc.getProductId(), rebuild.get(rc.getProductId()) + rc.getItemsSold());
                continue;
            }
            rebuild.put(rc.getProductId(), rc.getItemsSold());
        }
        return Collections.max(rebuild.entrySet(), Comparator.comparingInt(Map.Entry::getValue)).getKey();
    }

    protected String getIdOfItemWithLargestTotalSales() {
        HashMap<String, Double> sales = new LinkedHashMap<>();
        for (SalesRecord rc : salesRecords) {
            if (!sales.containsKey(rc.getProductId())) {
                sales.put(rc.getProductId(), this.getTotalSalesByProductId(rc.getProductId()));
            }
        }
        Map.Entry<String, Double> maxEntry = null;

        for (Map.Entry<String, Double> en : sales.entrySet()) {
            if (maxEntry == null ||
                    maxEntry.getValue().compareTo(en.getValue()) < 0
            ) {
                maxEntry = en;
            }
        }
        assert maxEntry != null;
        return maxEntry.getKey();
    }
}

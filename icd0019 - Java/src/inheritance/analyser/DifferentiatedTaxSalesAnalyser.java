package inheritance.analyser;

import java.util.List;
import java.util.Objects;

public final class DifferentiatedTaxSalesAnalyser extends SalesAnalyser {

    public DifferentiatedTaxSalesAnalyser(List<SalesRecord> records) {
        super(records);
    }

    @Override
    protected Double getTotalSales() {
        double totalSales = 0;
        for (SalesRecord rc : salesRecords) {
            if (rc.hasReducedRate()) {
                totalSales += rc.getItemsSold() * rc.getProductPrice() / 1.1;
            } else {
                totalSales += rc.getItemsSold() * rc.getProductPrice() / 1.2;
            }
        }
        return totalSales;
    }

    @Override
    protected Double getTotalSalesByProductId(String id) {
        double totalSales = 0;
        for (SalesRecord rc : salesRecords) {
            if (Objects.equals(rc.getProductId(), id)) {
                if (rc.hasReducedRate()) {
                    totalSales += rc.getItemsSold() * rc.getProductPrice() / 1.1;
                } else {
                    totalSales += rc.getItemsSold() * rc.getProductPrice() / 1.2;
                }
            }
        }
        return totalSales;
    }
}

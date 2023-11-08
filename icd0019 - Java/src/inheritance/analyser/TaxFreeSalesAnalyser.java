package inheritance.analyser;

import java.util.List;

public final class TaxFreeSalesAnalyser extends SalesAnalyser {

    public TaxFreeSalesAnalyser(List<SalesRecord> records) {
        super(records);
    }

    @Override
    protected Double getTotalSales() {
        double totalSales = 0;
        for (SalesRecord rc : salesRecords) {
            totalSales += rc.getItemsSold() * rc.getProductPrice();
        }
        return totalSales;
    }
}

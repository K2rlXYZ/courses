package inheritance.analyser;

import java.util.LinkedList;
import java.util.List;

public final class FlatTaxSalesAnalyser extends SalesAnalyser {

    public FlatTaxSalesAnalyser(List<SalesRecord> records) {
        super(records);
    }

    @Override
    protected Double getTotalSales() {
        double totalSales = 0;
        for (SalesRecord rc : salesRecords) {
            totalSales += rc.getItemsSold() * rc.getProductPrice();
        }
        return totalSales / 1.2;
    }

    @Override
    protected Double getTotalSalesByProductId(String id) {
        return super.getTotalSalesByProductId(id) / 1.2;
    }

}

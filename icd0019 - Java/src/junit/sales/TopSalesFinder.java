package junit.sales;

public class TopSalesFinder {
    private SalesRecord[] database;

    public TopSalesFinder() {
        database = new SalesRecord[]{};
    }

    public void registerSale(SalesRecord record) {
        // store sales record for later analyses by findItemsSoldOver()
        SalesRecord[] temp = new SalesRecord[database.length + 1];
        for (int x = 0; x < database.length; x++) {
            temp[x] = database[x];
        }
        temp[temp.length - 1] = record;
        database = temp;
    }

    public String[] findAllIdsFromDatabase(){
        String[] allIds = {};
        for (SalesRecord sr : database) {
            boolean noneMatch = true;
            for (String id : allIds) {
                if (id.equals(sr.getProductId())) {
                    noneMatch = false;
                }
            }
            if (noneMatch) {
                String[] temp = new String[allIds.length + 1];
                for (int x = 0; x < allIds.length; x++) {
                    temp[x] = allIds[x];
                }
                temp[temp.length - 1] = sr.getProductId();
                allIds = temp;
            }
        }
        return allIds;
    }

    public String[] findItemsSoldOver(int amount) {
        // find ids of records that sold over specified amount.
        String[] allIds = findAllIdsFromDatabase();
        String[] soldOverIds = {};
        for (String id : allIds) {
            int sold = 0;
            for (SalesRecord sr : database) {
                if (id.equals(sr.getProductId())) {
                    sold += sr.getItemsSold() * sr.getProductPrice();
                }
            }
            if (sold > amount) {
                String[] temp = new String[soldOverIds.length + 1];
                for (int x = 0; x < soldOverIds.length; x++) {
                    temp[x] = soldOverIds[x];
                }
                temp[temp.length - 1] = id;
                soldOverIds = temp;
            }
        }
        return soldOverIds;
    }

}



package fp.sales;

import java.io.File;
import java.io.FileNotFoundException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.function.Consumer;
import java.util.regex.Pattern;

public class Repository {

    private static final String FILE_PATH = "src/fp/sales/sales-data.csv";

    private DateTimeFormatter formatter = DateTimeFormatter
            .ofPattern("dd.MM.yyyy");

    public List<Entry> getEntries() {
        List<Entry> entries = new ArrayList<>();
        try {
            Scanner sc = new Scanner(new File(FILE_PATH));
            sc.findAll(".*").skip(1).map(i -> i.group(0)).forEach(string -> {
                if(!string.equals("")){
                    String[] s = string.split("\t");
                    if (s.length > 0) {
                        Entry e = new Entry();
                        e.setDate(LocalDate.parse(s[0], formatter));
                        e.setState(s[1]);
                        e.setProductId(s[2]);
                        e.setCategory(s[3]);
                        e.setAmount(Double.parseDouble(s[5].replace(",", ".")));
                        entries.add(e);
                    }
                }
            });
            return entries;
        } catch (Exception e) {
            System.out.println(e);
        }
        return entries;
    }

}

package poly.customer;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Scanner;

public class CustomerRepository {

    private static final String FILE_PATH = "src/poly/customer/data.txt";

    private List<AbstractCustomer> customers = new ArrayList<>();

    CustomerRepository() {
        try {
            File f = new File(FILE_PATH);
            Scanner sc = new Scanner(f);
            while (sc.hasNextLine()) {
                String[] line = sc.nextLine().split(";");
                if (line[0].equals("GOLD")) {
                    AbstractCustomer c = new GoldCustomer(line[1], line[2], Integer.parseInt(line[3]));
                    if (customers.stream().filter(i -> i.equals(c)).toList().isEmpty()) {
                        customers.add(c);
                    }
                } else if (line[0].equals("REGULAR")) {
                    AbstractCustomer c = new RegularCustomer(line[1], line[2], Integer.parseInt(line[3]), LocalDate.parse(line[4], DateTimeFormatter.ofPattern("yyyy-MM-dd")));
                    if (customers.stream().filter(i -> i.equals(c)).toList().isEmpty()) {
                        customers.add(c);
                    }
                }
            }
        } catch (FileNotFoundException fe) {
            System.out.println(fe);
        }
    }

    public Optional<AbstractCustomer> getCustomerById(String id) {
        return customers.stream().filter(i -> i.id.equals(id)).findFirst();
    }

    public void remove(String id) {
        customers = customers.stream().filter(i -> !i.id.equals(id)).toList();
        try {
            FileWriter fw = new FileWriter(FILE_PATH, false);
            StringBuilder finalAdd = new StringBuilder();
            for (AbstractCustomer ac : customers) {
                String clas = ac.getClass().toString().equals("class poly.customer.RegularCustomer") ? "REGULAR" : "GOLD";
                String addTxt = ac.getClass().toString().equals("class poly.customer.RegularCustomer") ?
                        clas + ";" + ac.id + ";" + ac.name + ";" + ac.bonusPoints + ";" + ac.lastOrdDate :
                        clas + ";" + ac.id + ";" + ac.name + ";" + ac.bonusPoints;
                finalAdd.append(addTxt).append("\n");
            }
            fw.append(finalAdd);
            fw.close();
        } catch (IOException ie) {
            System.out.println(ie);
        }
    }

    public void save(AbstractCustomer customer) {
        if (customers.stream().filter(i -> i.equals(customer) && i.getBonusPoints()==customer.getBonusPoints()).toList().isEmpty()) {
            try {
                customers.add(customer);
                FileWriter fw = new FileWriter(FILE_PATH, false);
                StringBuilder finalAdd = new StringBuilder();
                for (AbstractCustomer ac : customers) {
                    String clas = ac.getClass().toString().equals("class poly.customer.RegularCustomer") ? "REGULAR" : "GOLD";
                    String addTxt = ac.getClass().toString().equals("class poly.customer.RegularCustomer") ?
                            clas + ";" + ac.id + ";" + ac.name + ";" + ac.bonusPoints + ";" + ac.lastOrdDate :
                            clas + ";" + ac.id + ";" + ac.name + ";" + ac.bonusPoints;
                    finalAdd.append(addTxt).append("\n");
                }
                fw.append(finalAdd);
                fw.close();
            } catch (IOException ie) {
                System.out.println(ie);
            }
        }
    }

    public int getCustomerCount() {
        return customers.size();
    }
}

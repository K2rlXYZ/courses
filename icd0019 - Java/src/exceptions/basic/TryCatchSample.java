package exceptions.basic;

import java.nio.file.Files;
import java.nio.file.Paths;

public class TryCatchSample {


    public String readDataFrom(Resource resource) {
        try {
            resource.open();
            String data = resource.read();
            System.out.println(data);
            resource.close();
            return data;
        } catch (Exception exception) {
            resource.close();
            return "someDefaultValue";
        }
    }
}

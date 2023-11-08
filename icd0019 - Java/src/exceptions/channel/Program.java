package exceptions.channel;

import java.io.IOException;

public class Program {

    ConstantProvider provider = new ConstantProvider();

    public static void main(String[] args) {

        Program program = new Program();

//        program.provider.makeItThrowMissingConstantException();
//        program.provider.makeItThrowCorruptConfigurationException();

        program.main(7); // 7 is arbitrary value
    }

    public void main(int input) {
        try {
            double result = (input + 42) * provider.getMultiplier2();

            String formatted = format(String.valueOf(result));

            present(formatted);
        } catch (MissingConstantException e) {
            present(formatError("Constant is missing"));
        } catch (CorruptConfigurationException e) {
            present(formatError("Configuration file is corrupt"));
        } catch (IOException e) {
            present(e.getMessage());
        }


    }

    private String format(String data) {
        return "### Result is %s ###".formatted(data);
    }

    private String formatError(String message) {
        return "### Error: %s ###".formatted(message);
    }

    private void present(String data) {
        System.out.println(data);
    }
}

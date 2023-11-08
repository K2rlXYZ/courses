package exceptions.numbers;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class NumberConverter {
    private Properties properties;

    public NumberConverter(String lang) {
        String filePath = "src/exceptions/numbers/numbers_%s.properties";

        properties = new Properties();
        FileInputStream is = null;

        try {
            is = new FileInputStream(String.format(filePath, lang));

            InputStreamReader reader = new InputStreamReader(is, StandardCharsets.UTF_8);

            properties.load(reader);

        } catch (IOException e) {
            throw new MissingLanguageFileException(lang, e);
        } catch (IllegalArgumentException e) {
            throw new BrokenLanguageFileException(lang, e);
        } finally {
            close(is);
        }
    }

    private static void close(FileInputStream is) {
        if (is == null) {
            return;
        }

        try {
            is.close();
        } catch (IOException ignore) {
        }
    }

    public String numberInWords(Integer number) {
        if (properties.containsKey(number.toString())) {
            return properties.getProperty(number.toString());
        }
        int ones = number % 10;
        int tens = (number / 10) % 10;
        int hundreds = (number / 100) % 10;
        StringBuilder numberAsText = new StringBuilder();
        if (hundreds != 0) {
            numberAsText.append(stringifyHundreds(hundreds, tens, ones));
        }
        if (tens != 0) {
            if (properties.containsKey(String.valueOf(tens * 10 + ones))) {
                numberAsText.append(properties.getProperty(String.valueOf(tens * 10 + ones)));
                return numberAsText.toString();
            }
            if (tens == 1) {
                numberAsText.append(properties.getProperty(String.valueOf(ones)) + properties.getProperty("teen"));
                return numberAsText.toString();
            }
            numberAsText.append(stringifyTens(hundreds, tens, ones));
        }
        if (ones != 0) {
            numberAsText.append(properties.getProperty(String.valueOf(ones)));
        }
        if (numberAsText.toString().contains("null") && !properties.containsKey("0")) {
            throw new MissingTranslationException(String.valueOf(number));
        }
        return numberAsText.toString();
    }

    private String stringifyHundreds(int hundreds, int tens, int ones) {
        StringBuilder returnString = new StringBuilder();
        returnString.append(properties.getProperty(String.valueOf(hundreds)) +
                properties.getProperty("hundreds-before-delimiter") + properties.getProperty("hundred"));
        if (tens != 0 || ones != 0) {
            returnString.append(properties.getProperty("hundreds-after-delimiter"));
        }
        return returnString.toString();
    }

    private String stringifyTens(int hundreds, int tens, int ones) {
        StringBuilder returnString = new StringBuilder();
        if (properties.containsKey(String.valueOf(tens * 10))) {
            returnString.append(properties.getProperty(String.valueOf(tens * 10)));
        } else {
            returnString.append(properties.getProperty(String.valueOf(tens)) +
                    properties.getProperty("tens-suffix"));
        }
        if (ones != 0) {
            returnString.append(properties.getProperty("tens-after-delimiter"));
        }
        return returnString.toString();
    }
}

package exceptions.bad;

public class BadTryCatch {

    public boolean containsSingleLetters(String input) {

        int index = 0;

        try {
            while (index+1 < input.length()) {
                if (input.charAt(index) == input.charAt(index + 1)) {
                    return false;
                }
                index++;
            }
        } catch (Exception e) {
            return false;
        }

        return true;
    }


}

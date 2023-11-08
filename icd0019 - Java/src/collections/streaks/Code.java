package collections.streaks;

import java.util.*;

public class Code {

    public static List<List<String>> getStreakList(String input) {
        List<List<String>> arr = new ArrayList<>();
        if (input == "") {
            return arr;
        }
        List<String> myList = new ArrayList<String>(Arrays.asList(input.split("")));
        System.out.println(myList);

        List<String> temp = new ArrayList<>();
        for (int x = 0; x < myList.size(); x++) {
            temp.add(myList.get(x));
            if (x == myList.size()-1||!Objects.equals(myList.get(x + 1), myList.get(x))) {
                arr.add(temp);
                temp = new ArrayList<>();
                temp.clear();
            }
        }
        return arr;
    }


}

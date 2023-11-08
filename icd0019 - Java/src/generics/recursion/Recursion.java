package generics.recursion;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Recursion {

    public List<String> getParts(Path path) {

        // a)
        List<String> elements = new ArrayList<>();
        elements.add(path.toString());
        Path parent = path.getParent();
        while (parent != null) {
            elements.add(parent.toString());
            parent = parent.getParent();
        }
        return elements;
    }

    public List<String> getParts2(Path path) {
        // b)
        System.out.println(path.toString());
        Path parent = path.getParent();
        if (parent != null) {
            getParts2(parent);
        }
        return null;
    }

    public List<String> getParts3(Path path, List<String> elements) {
        // c)

        elements.add(path.toString());
        Path parent = path.getParent();
        if (parent != null) {
            elements = getParts3(parent, elements);
        }
        return elements;
    }

    public List<String> getParts4(Path path) {
        // d)

        List<String> elements = new ArrayList<>();
        elements.add(path.toString());
        Path parent = path.getParent();
        if (parent != null) {
            elements = getParts4(parent, elements);
        }
        System.out.println(elements);
        return elements;
    }

    public List<String> getParts4(Path path, List<String> elements) {
        // d)

        elements.add(path.toString());
        Path parent = path.getParent();
        if (parent != null) {
            elements = getParts4(parent, elements);
        }
        return elements;
    }
}

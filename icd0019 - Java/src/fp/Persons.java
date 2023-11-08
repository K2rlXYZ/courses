package fp;

import org.junit.Test;

import java.util.*;
import java.util.stream.Collectors;


public class Persons {

    private List<Person> persons = List.of(
            new Person(1, "Alice", 22),
            new Person(2, "Bob", 20),
            new Person(3, "Carol", 21));

    @Test
    public void findsPersonById() {
        Person person = persons.stream().filter(p -> p.getId() == 2).toList().get(0);
        System.out.println(person);
    }

    @Test
    public void removePersonById() {
        System.out.println(persons);
        var newl = persons.stream().filter(p -> p.getId() != 2).toList();
        System.out.println(newl);
    }

    @Test
    public void findsPersonNames() {
        System.out.println(persons.stream().map(Person::getName).collect(Collectors.joining(", ")));
    }

    @Test
    public void reverseSortedByAge() {
        var newl = persons.stream().sorted(Comparator.comparing(Person::getAge).reversed()).toList();
        System.out.println(newl);
    }

}

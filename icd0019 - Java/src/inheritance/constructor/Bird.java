package inheritance.constructor;

public class Bird {
    public Bird (){

        System.out.println("constructing Bird");
    }
    public Bird(String color) {
        System.out.println("constructing " + color + " Bird");

        // init stuff that is common for all the birds
    }
}

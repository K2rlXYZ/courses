package generics.stack;

public class Stack<T> {
    private T[] elements;
    private Integer size = 0;

    public Stack() {
        elements = (T[]) (new Object[100]);
    }

    public void push(T element) {
        elements[size++] = element;
    }

    @SuppressWarnings("unchecked")
    public T pop() {
        if (size == 0) {
            throw new IllegalStateException("stack is empty");
        }

        return elements[--size];
    }

}

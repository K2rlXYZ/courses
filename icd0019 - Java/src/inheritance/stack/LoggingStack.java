package inheritance.stack;

import java.util.Stack;

public class LoggingStack extends Stack<Integer> {
    @Override
    public Integer push(Integer i){
        System.out.println("Pushed " + String.valueOf(i));
        return super.push(i);
    }

    @Override
    public synchronized int size() {
        System.out.println("Checking the size of the stack");
        return super.size();
    }

    public void pushAll(Integer... numbers){
        for (Integer nr:numbers) {
            this.push(nr);
        }
    }
}

package inheritance.sender;

import java.time.LocalTime;

public class EmailLetterSender extends Sender {
    public EmailLetterSender(LocalTime currentTime) {
        super(currentTime);
        this.currentTime = currentTime;
    }
}
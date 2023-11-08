package inheritance.sender;

import java.time.LocalTime;

public class SmsLetterSender extends Sender {

    public SmsLetterSender(LocalTime currentTime) {
        super(currentTime);
        this.currentTime = currentTime;
    }


}

package inheritance.sender;

import java.time.LocalTime;

public class Sender {

    public LocalTime currentTime;

    public Sender(LocalTime currentTime) {
        this.currentTime = currentTime;
    }
    public void sendLetter() {
        String greeting = "Good " + getTimeOfDayString();
        String contents = "Dead customer, ...";

        // simulate sending the sms

        System.out.println("Sending sms ...");
        System.out.println("Title: " + greeting);
        System.out.println("Text: " + contents);
    }

    private String getTimeOfDayString() {

        int hour = currentTime.getHour();

        if (hour > 5 && hour <= 11) {
            return "morning";
        } else if (hour > 11 && hour <= 17) {
            return "afternoon";
        } else if (hour > 17 && hour <= 20) {
            return "evening";
        } else {
            return "night";
        }
    }
}

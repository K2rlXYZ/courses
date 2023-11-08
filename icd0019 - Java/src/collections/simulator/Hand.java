package collections.simulator;

import java.util.*;

public class Hand implements Iterable<Card>, Comparable<Hand> {

    private List<Card> cards = new ArrayList<>();

    public void addCard(Card card) {
        cards.add(card);
    }

    @Override
    public String toString() {
        return cards.toString();
    }

    Card.CardValue[] cardValues = new Card.CardValue[Card.CardValue.values().length + 1];

    public HandType getHandType() {
        cardValues[0] = Card.CardValue.A;
        for (int x = 1; x < Card.CardValue.values().length + 1; x++) {
            cardValues[x] = Card.CardValue.values()[x - 1];
        }
        switch (cards.size()) {
            case 5:
                if (straightFlushCheck()) {
                    return HandType.STRAIGHT_FLUSH;
                } else if (straightCheck()) {
                    return HandType.STRAIGHT;
                } else if (fullHouseCheck()) {
                    return HandType.FULL_HOUSE;
                } else if (flushCheck()) {
                    return HandType.FLUSH;
                }
            case 4:
                if (fourOfAKindCheck()) {
                    return HandType.FOUR_OF_A_KIND;
                } else if (twoPairCheck()) {
                    return HandType.TWO_PAIRS;
                }
            case 3:
                if (tripsCheck()) {
                    return HandType.TRIPS;
                }
            case 2:
                if (onePairCheck()) {
                    return HandType.ONE_PAIR;
                }
            default:
        }
        return null;
    }

    public boolean straightFlushCheck() {
        //STRAIGHT FLUSH
        for (int x = 0; x < cardValues.length - 4; x++) {
            int finalX = x;
            for (Card.CardSuit s : Card.CardSuit.values()) {
                if (cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX]) && i.getSuit() == s) &&
                        cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX + 1]) && i.getSuit() == s) &&
                        cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX + 2]) && i.getSuit() == s) &&
                        cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX + 3]) && i.getSuit() == s) &&
                        cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX + 4]) && i.getSuit() == s)
                ) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean straightCheck() {
        //STRAIGHT
        for (int x = 0; x < cardValues.length - 4; x++) {
            int finalX = x;
            if (cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX])) &&
                    cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX + 1])) &&
                    cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX + 2])) &&
                    cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX + 3])) &&
                    cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX + 4]))
            ) {
                return true;
            }
        }
        return false;
    }

    public boolean fullHouseCheck() {

        //FULL HOUSE
        for (int x = 0; x < cardValues.length; x++) {
            int finalX = x;
            List<Card> cardsCopy = new ArrayList<>(cards);
            if (cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX]))
            ) {
                for (int y = 0; true; y++) {
                    Optional<Card> c = cardsCopy.stream().filter(i -> i.getValue().equals(cardValues[finalX])).findAny();
                    if (c.isEmpty()) {
                        break;
                    }
                    cardsCopy.remove(c.get());
                    if (y == 2) {
                        return fullHouseCheckSecondDepth(cardsCopy);
                    }
                }
            }
        }
        return false;
    }

    private boolean fullHouseCheckSecondDepth(List<Card> cardsCopy) {
        for (int x2 = 0; x2 < cardValues.length; x2++) {
            int finalX2 = x2;
            if (cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX2]))
            ) {
                for (int y2 = 0; true; y2++) {
                    Optional<Card> c2 = cardsCopy.stream().filter(i -> i.getValue().equals(cardValues[finalX2])).findAny();
                    if (c2.isEmpty()) {
                        break;
                    }
                    cardsCopy.remove(c2.get());
                    if (y2 == 1) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public boolean flushCheck() {
        //FLUSH
        for (Card.CardSuit s : Card.CardSuit.values()) {
            if (cards.stream().allMatch(i -> i.getSuit() == s)) {
                return true;
            }
        }
        return false;
    }

    public boolean fourOfAKindCheck() {
        //FOUR OF A KIND
        for (int x = 0; x < cardValues.length; x++) {
            int finalX = x;
            List<Card> cardsCopy = new ArrayList<>(cards);
            if (cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX]))
            ) {
                for (int y = 0; true; y++) {
                    Optional<Card> c = cardsCopy.stream().filter(i -> i.getValue().equals(cardValues[finalX])).findAny();
                    if (c.isEmpty()) {
                        break;
                    }
                    cardsCopy.remove(c.get());
                    if (y == 3) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public boolean twoPairCheck() {
        //TWO PAIRS
        for (int x = 0; x < cardValues.length; x++) {
            int finalX = x;
            List<Card> cardsCopy = new ArrayList<>(cards);
            if (cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX]))
            ) {
                for (int y = 0; true; y++) {
                    Optional<Card> c = cardsCopy.stream().filter(i -> i.getValue().equals(cardValues[finalX])).findAny();
                    if (c.isEmpty()) {
                        break;
                    }
                    cardsCopy.remove(c.get());
                    if (y == 1) {
                        return twoPairCheckSecondDepth(cardsCopy);
                    }
                }
            }
        }
        return false;
    }

    private boolean twoPairCheckSecondDepth(List<Card> cardsCopy) {
        for (int x2 = 0; x2 < cardValues.length; x2++) {
            int finalX2 = x2;
            if (cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX2]))
            ) {
                for (int y2 = 0; true; y2++) {
                    Optional<Card> c2 = cardsCopy.stream().filter(i -> i.getValue().equals(cardValues[finalX2])).findAny();
                    if (c2.isEmpty()) {
                        break;
                    }
                    cardsCopy.remove(c2.get());
                    if (y2 == 1) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public boolean tripsCheck() {
        //TRIPS
        for (int x = 0; x < cardValues.length; x++) {
            int finalX = x;
            List<Card> cardsCopy = new ArrayList<>(cards);
            if (cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX]))
            ) {
                for (int y = 0; true; y++) {
                    Optional<Card> c = cardsCopy.stream().filter(i -> i.getValue().equals(cardValues[finalX])).findAny();
                    if (c.isEmpty()) {
                        break;
                    }
                    cardsCopy.remove(c.get());
                    if (y == 2) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public boolean onePairCheck() {
        //ONE PAIR
        for (int x = 0; x < cardValues.length; x++) {
            int finalX = x;
            List<Card> cardsCopy = new ArrayList<>(cards);
            if (cards.stream().anyMatch(i -> i.getValue().equals(cardValues[finalX]))
            ) {
                for (int y = 0; true; y++) {
                    Optional<Card> c = cardsCopy.stream().filter(i -> i.getValue().equals(cardValues[finalX])).findAny();
                    if (c.isEmpty()) {
                        break;
                    }
                    cardsCopy.remove(c.get());
                    if (y == 1) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public boolean contains(Card card) {
        return cards.contains(card);
    }

    public boolean isEmpty() {
        return cards.isEmpty();
    }

    @Override
    public Iterator<Card> iterator() {
        return cards.iterator();
    }

    @Override
    public int compareTo(Hand other) {
        return 0;
    }
}

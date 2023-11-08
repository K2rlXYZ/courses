package poly.customer;

import java.time.LocalDate;
import java.util.Objects;

public final class RegularCustomer extends AbstractCustomer {

    public RegularCustomer(String id, String name,
                           int bonusPoints, LocalDate lastOrderDate) {

        super(id, name, bonusPoints);

        this.lastOrdDate = lastOrderDate;
    }

    @Override
    public void collectBonusPointsFrom(Order order) {
        if (order.getTotal() < 100) {
            return;
        }
        if (this.lastOrdDate.getMonth().getValue() - order.getDate().getMonth().getValue() >= 0) {
            this.bonusPoints += order.getTotal() * 1.5;
        } else {
            this.bonusPoints += order.getTotal();
        }
        this.lastOrdDate = order.getDate();
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null || this.getClass() != obj.getClass()) {
            return false;
        }

        RegularCustomer other = (RegularCustomer) obj;

        return Objects.equals(id, other.id) &&
                Objects.equals(name, other.name) &&
                Objects.equals(bonusPoints, other.bonusPoints) &&
                Objects.equals(lastOrdDate, other.lastOrdDate);
    }

    @Override
    public int hashCode() {
        return this.id.hashCode() + Objects.hash(this.bonusPoints) + this.name.hashCode() +
                this.lastOrdDate.hashCode() + this.getClass().hashCode();
    }

    @Override
    public String asString() {
        return this.getClass() + " Id: " + this.id + " Name: " + this.name + " Bonus Points: " + this.bonusPoints +
                " Last Order Date: " + lastOrdDate.toString();
    }

}
package poly.customer;

import java.util.Objects;

public final class GoldCustomer extends AbstractCustomer {

    public GoldCustomer(String id, String name, int bonusPoints) {
        super(id, name, bonusPoints);
    }

    @Override
    public void collectBonusPointsFrom(Order order) {
        if (order.getTotal() < 100) {
            return;
        }
        bonusPoints += order.getTotal() * 1.5;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null || this.getClass() != obj.getClass()) {
            return false;
        }

        GoldCustomer other = (GoldCustomer) obj;

        return Objects.equals(id, other.id) &&
                Objects.equals(name, other.name) &&
                Objects.equals(bonusPoints, other.bonusPoints);
    }

    @Override
    public int hashCode() {
        return this.id.hashCode() + Objects.hash(this.bonusPoints) + this.name.hashCode() + this.getClass().hashCode();
    }

    @Override
    public String asString() {
        return this.getClass() + " Id: " + this.id + " Name: " + this.name + " Bonus Points: " + this.bonusPoints;
    }

}
package oo.hide;

import org.hamcrest.collection.IsArrayContainingInAnyOrder;

import java.util.Arrays;

public class PointSet {
    private Point[] set;
    private int usedSpace;

    public PointSet(int capacity) {
        set = new Point[capacity];
        usedSpace = 0;
    }

    public PointSet() {
        this(0);
        usedSpace = 0;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null || obj.getClass() != this.getClass()) {
            return false;
        }
        PointSet other = (PointSet) obj;
        boolean equal = true;
        for (Point p : set) {
            if (!other.contains(p)) {
                equal = false;
            }
        }
        return equal;
    }

    public void add(Point point) {
        if (contains(point)) {
            return;
        }
        if (usedSpace == set.length) {
            Point[] temp;
            if (set.length == 0) {
                temp = new Point[1];
            } else {
                temp = new Point[set.length * 2];
            }
            for (int x = 0; x < set.length; x++) {
                temp[x] = set[x];
            }
            set = temp;
        }
        if (point == null) {
            usedSpace += 1;
            return;
        }
        set[usedSpace] = point;
        usedSpace += 1;
    }

    public int size() {
        return set.length;
    }

    public boolean contains(Point point) {
        for (Point p : set) {
            if (p != null && p.equals(point)) {
                return true;
            }
        }
        return false;
    }

    public PointSet subtract(PointSet other) {
        PointSet after = new PointSet();
        for (Point p : set) {
            if (!other.contains(p)) {
                after.add(p);
            }
        }
        return after;
    }

    public PointSet intersect(PointSet other) {
        PointSet after = new PointSet();
        for (Point p : set) {
            if (other.contains(p)) {
                after.add(p);
            }
        }
        return after;
    }

    public void remove(Point point) {
        for (int x = 0; x < set.length; x++) {
            if (set[x] != null && set[x].equals(point)) {
                for (int y = x; y < set.length; y++) {
                    if (y + 1 < set.length) {
                        set[y] = set[y + 1];
                    }
                }
            }
        }
    }

    @Override
    public String toString() {
        StringBuilder returanble = new StringBuilder();
        for (int x = 0; x < set.length; x++) {
            if (set[x] != null) {
                returanble.append(set[x].toString()).append(", ");
            } else {
                boolean allNulls = true;
                for (int y = x + 1; y < set.length; y++) {
                    if (set[y] != null) {
                        allNulls = false;
                        break;
                    }
                }
                if (!allNulls) {
                    returanble.append("null, ");
                }
            }
        }
        returanble.delete(returanble.length() - 2, returanble.length());
        return returanble.toString();
    }
}

import java.util.Comparator;

public class MyComparator implements Comparator<Object> {
    /**
     * Compares two objects for order. Returns a negative integer, zero, or a 
     * positive integer as the first argument is less than, equal to, or greater 
     * than the second.
     *
     * @param aObj1 the first object to compare
     * @param aObj2 the second object to compare
     * @return a negative integer, zero, or a positive integer as the first 
     *         argument is less than, equal to, or greater than the second
     */
    @Override
    public int compare(Object aObj1, Object aObj2) {
        if (aObj1 == null && aObj2 == null) {
            return 0;
        }
        if (aObj1 == null) {
            return -1;
        }
        if (aObj2 == null) {
            return 1;
        }
        if (aObj1 instanceof Comparable && aObj2 instanceof Comparable) {
            return ((Comparable) aObj1).compareTo(aObj2);
        }
        throw new IllegalArgumentException("Both objects must be comparable");
    }
}
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
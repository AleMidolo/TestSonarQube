public static int nullSafeHashCode(long[] array) {
    if (array == null) {
        return 0;
    }
    int result = 1;
    for (long element : array) {
        result = 31 * result + Long.hashCode(element);
    }
    return result;
}
public static double[] toPrimitive(final Double[] array) {
    if (array == null) {
        return null;
    }
    double[] result = new double[array.length];
    for (int i = 0; i < array.length; i++) {
        if (array[i] == null) {
            throw new NullPointerException("Element at index " + i + " is null");
        }
        result[i] = array[i];
    }
    return result;
}
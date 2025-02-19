public static Double[] toObject(final double[] array) {
    if (array == null) {
        return null;
    }
    Double[] result = new Double[array.length];
    for (int i = 0; i < array.length; i++) {
        result[i] = array[i]; // Autoboxing from double to Double
    }
    return result;
}
public static int[] toPrimitive(final Integer[] array) {
    if (array == null) {
        return null;
    }
    int[] result = new int[array.length];
    for (int i = 0; i < array.length; i++) {
        if (array[i] == null) {
            throw new NullPointerException("Element at index " + i + " is null");
        }
        result[i] = array[i].intValue();
    }
    return result;
}
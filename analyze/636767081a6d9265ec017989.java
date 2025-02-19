public static boolean[] toPrimitive(final Boolean[] array) {
    if (array == null) {
        return null;
    }
    boolean[] primitiveArray = new boolean[array.length];
    for (int i = 0; i < array.length; i++) {
        if (array[i] == null) {
            throw new NullPointerException("Element at index " + i + " is null");
        }
        primitiveArray[i] = array[i];
    }
    return primitiveArray;
}
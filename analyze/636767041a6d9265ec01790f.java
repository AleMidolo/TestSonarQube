public static Integer[] toObject(final int[] array) {
    if (array == null) {
        return null;
    }
    Integer[] result = new Integer[array.length];
    for (int i = 0; i < array.length; i++) {
        result[i] = Integer.valueOf(array[i]);
    }
    return result;
}
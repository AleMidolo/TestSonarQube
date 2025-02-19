public static Short[] toObject(final short[] array) {
    if (array == null) {
        return null;
    }
    Short[] result = new Short[array.length];
    for (int i = 0; i < array.length; i++) {
        result[i] = Short.valueOf(array[i]);
    }
    return result;
}
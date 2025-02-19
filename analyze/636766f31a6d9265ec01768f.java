public static char[] clone(final char[] array) {
    if (array == null) {
        return null;
    }
    char[] clonedArray = new char[array.length];
    System.arraycopy(array, 0, clonedArray, 0, array.length);
    return clonedArray;
}
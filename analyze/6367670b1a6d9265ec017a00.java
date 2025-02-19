public static boolean isSameLength(final byte[] array1, final byte[] array2) {
    int length1 = (array1 == null) ? 0 : array1.length;
    int length2 = (array2 == null) ? 0 : array2.length;
    return length1 == length2;
}
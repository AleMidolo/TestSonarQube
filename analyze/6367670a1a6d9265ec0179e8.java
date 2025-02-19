public static Boolean[] nullToEmpty(final Boolean[] array) {
    if (array == null || array.length == 0) {
        return new Boolean[0]; // Return an empty array if input is null or empty
    }
    return array; // Return the original array if it's not null or empty
}
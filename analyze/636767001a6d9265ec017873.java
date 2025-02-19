public static String reverse(final String str) {
    if (str == null) {
        return null;
    }
    return new StringBuilder(str).reverse().toString();
}
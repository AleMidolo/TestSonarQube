public static String toString(final char ch) {
    if (ch >= 0 && ch <= 127) {
        return String.valueOf(ch);
    }
    return new String(new char[]{ch});
}
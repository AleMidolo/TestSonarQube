public static boolean isAsciiControl(final char ch) {
    return ch < 32 || ch == 127;
}
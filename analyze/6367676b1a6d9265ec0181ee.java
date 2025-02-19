public static String trimTrailingWhitespace(String str) {
    if (str == null) {
        return null;
    }
    int end = str.length();
    while (end > 0 && Character.isWhitespace(str.charAt(end - 1))) {
        end--;
    }
    return str.substring(0, end);
}
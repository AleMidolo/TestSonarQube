public static String trimLeadingWhitespace(String str) {
    if (str == null) {
        return null;
    }
    int index = 0;
    while (index < str.length() && Character.isWhitespace(str.charAt(index))) {
        index++;
    }
    return str.substring(index);
}
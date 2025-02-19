public static String sub(String str, int start, int end) {
    if (str == null) {
        return null;
    }
    if (start < 0) {
        start = 0;
    }
    if (end > str.length()) {
        end = str.length();
    }
    if (start > end) {
        return "";
    }
    return str.substring(start, end);
}
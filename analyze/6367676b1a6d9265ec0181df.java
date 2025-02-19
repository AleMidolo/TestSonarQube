public static boolean startsWithIgnoreCase(String str, String prefix) {
    if (str == null || prefix == null) {
        return false;
    }
    if (prefix.length() > str.length()) {
        return false;
    }
    return str.substring(0, prefix.length()).equalsIgnoreCase(prefix);
}
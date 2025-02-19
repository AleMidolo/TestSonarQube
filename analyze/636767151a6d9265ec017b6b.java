private static boolean startsWith(final String str, final String prefix, final boolean ignoreCase) {
    if (str == null && prefix == null) {
        return true;
    }
    if (str == null || prefix == null) {
        return false;
    }
    if (ignoreCase) {
        return str.toLowerCase().startsWith(prefix.toLowerCase());
    } else {
        return str.startsWith(prefix);
    }
}
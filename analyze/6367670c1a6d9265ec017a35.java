private static boolean endsWith(final String str, final String suffix, final boolean ignoreCase) {
    if (str == null && suffix == null) {
        return true;
    }
    if (str == null || suffix == null) {
        return false;
    }
    if (ignoreCase) {
        return str.toLowerCase().endsWith(suffix.toLowerCase());
    } else {
        return str.endsWith(suffix);
    }
}
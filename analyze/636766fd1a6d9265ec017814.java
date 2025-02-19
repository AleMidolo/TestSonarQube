public static boolean arrayequals(byte[] a, byte[] b, int count) {
    if (a == null || b == null || count < 0 || count > a.length || count > b.length) {
        return false;
    }
    for (int i = 0; i < count; i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}
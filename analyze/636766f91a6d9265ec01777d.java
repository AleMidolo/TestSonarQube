public static byte convertHexDigit(byte b) {
    if (b >= '0' && b <= '9') {
        return (byte) (b - '0');
    } else if (b >= 'a' && b <= 'f') {
        return (byte) (b - 'a' + 10);
    } else if (b >= 'A' && b <= 'F') {
        return (byte) (b - 'A' + 10);
    } else {
        throw new IllegalArgumentException("Input must be a hex digit (0-9, a-f, A-F)");
    }
}
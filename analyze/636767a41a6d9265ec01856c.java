public static int computeUTF8Size(final CharSequence str, final int index, final int len) {
    int size = 0;
    for (int i = index; i < index + len; i++) {
        char c = str.charAt(i);
        if (c < 0x80) {
            size += 1; // 1 byte for ASCII characters
        } else if (c < 0x800) {
            size += 2; // 2 bytes for characters in the range 0x80 to 0x7FF
        } else if (c < 0x10000) {
            size += 3; // 3 bytes for characters in the range 0x800 to 0xFFFF
        } else {
            size += 4; // 4 bytes for characters in the range 0x10000 and above
        }
    }
    return size;
}
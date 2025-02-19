public long readLong(final int offset) {
    // Assuming ClassReader has a method to read bytes from a specific offset
    // and that it reads 8 bytes for a long value.
    byte[] bytes = new byte[8];
    for (int i = 0; i < 8; i++) {
        bytes[i] = readByte(offset + i); // readByte is a hypothetical method to read a byte
    }
    return ((long) bytes[0] << 56) |
           ((long) (bytes[1] & 255) << 48) |
           ((long) (bytes[2] & 255) << 40) |
           ((long) (bytes[3] & 255) << 32) |
           ((long) (bytes[4] & 255) << 24) |
           ((bytes[5] & 255) << 16) |
           ((bytes[6] & 255) << 8) |
           (bytes[7] & 255);
}
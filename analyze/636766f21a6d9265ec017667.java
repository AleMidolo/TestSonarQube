public short readShort(final int offset) {
    // Assuming ClassReader has a method to read bytes from a specific offset
    // and that it reads two bytes for a short value.
    byte[] data = classReader.getData(); // Get the byte array from ClassReader
    return (short) ((data[offset] << 8) | (data[offset + 1] & 0xFF));
}
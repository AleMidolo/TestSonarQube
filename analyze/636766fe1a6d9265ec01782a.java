final String readUtf(final int constantPoolEntryIndex, final char[] charBuffer) {
    // Assuming classFileBuffer is a byte array that contains the class file data
    int length = ((classFileBuffer[constantPoolEntryIndex] & 0xFF) << 8) | (classFileBuffer[constantPoolEntryIndex + 1] & 0xFF);
    int offset = constantPoolEntryIndex + 2;

    for (int i = 0; i < length; i++) {
        charBuffer[i] = (char) ((classFileBuffer[offset + i * 2] & 0xFF) << 8 | (classFileBuffer[offset + i * 2 + 1] & 0xFF));
    }

    return new String(charBuffer, 0, length);
}
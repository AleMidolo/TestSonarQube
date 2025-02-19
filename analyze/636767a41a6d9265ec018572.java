public long readRawVarint64() throws IOException {
    long result = 0;
    int shift = 0;
    while (true) {
        byte b = readByte(); // Assume readByte() reads a byte from the stream
        result |= ((long)(b & 0x7F)) << shift;
        if ((b & 0x80) == 0) {
            break;
        }
        shift += 7;
        if (shift >= 64) {
            throw new IOException("Varint is too long");
        }
    }
    return result;
}
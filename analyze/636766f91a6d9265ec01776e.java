@Override 
public void write(final byte b[], final int off, final int len) throws IOException {
    if (b == null) {
        throw new NullPointerException("Byte array is null");
    }
    if (off < 0 || len < 0 || off + len > b.length) {
        throw new IndexOutOfBoundsException("Invalid offset or length");
    }
    for (int i = 0; i < len; i++) {
        // Assuming there's a method to write a single byte to the output stream
        writeByte(b[off + i]);
    }
}

private void writeByte(byte value) throws IOException {
    // Implementation for writing a single byte to the output stream
}
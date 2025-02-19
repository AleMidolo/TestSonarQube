public byte readByte() throws IOException {
    if (buffer == null || position >= buffer.length) {
        fillBuffer();
    }
    if (position >= buffer.length) {
        throw new IOException("No more data available");
    }
    return buffer[position++];
}

private void fillBuffer() throws IOException {
    // Implement the logic to read data from the input stream into the buffer
    // For example:
    int bytesRead = inputStream.read(buffer);
    if (bytesRead == -1) {
        buffer = null; // No more data
    } else {
        position = 0; // Reset position to the start of the buffer
    }
}
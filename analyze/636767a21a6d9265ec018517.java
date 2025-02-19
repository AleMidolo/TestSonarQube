public final byte[] toByteArray() {
    // Assuming there is a list of byte arrays representing the buffers
    List<byte[]> buffers = getBuffers(); // Method to retrieve the buffers
    int totalLength = 0;

    // Calculate the total length of the resulting byte array
    for (byte[] buffer : buffers) {
        totalLength += buffer.length;
    }

    // Create a new byte array to hold all the contents
    byte[] result = new byte[totalLength];
    int currentIndex = 0;

    // Copy each buffer's contents into the result array
    for (byte[] buffer : buffers) {
        System.arraycopy(buffer, 0, result, currentIndex, buffer.length);
        currentIndex += buffer.length;
    }

    return result;
}
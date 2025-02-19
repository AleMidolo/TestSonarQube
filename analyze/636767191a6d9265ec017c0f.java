private void enlarge(final int size) {
    if (size < 0) {
        throw new IllegalArgumentException("Size must be non-negative");
    }
    
    int currentLength = byteArray.length; // Assuming byteArray is the current byte array
    int newLength = currentLength + size;
    
    byte[] newArray = new byte[newLength];
    System.arraycopy(byteArray, 0, newArray, 0, currentLength);
    byteArray = newArray; // Update the reference to the new array
}
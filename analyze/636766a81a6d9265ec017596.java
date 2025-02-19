public ByteVector putInt(final int intValue) {
    // Check if the internal array needs to be resized
    if (size + Integer.BYTES > byteArray.length) {
        resize(byteArray.length + Integer.BYTES);
    }
    
    // Insert the integer into the byte array
    byteArray[size++] = (byte) (intValue >> 24);
    byteArray[size++] = (byte) (intValue >> 16);
    byteArray[size++] = (byte) (intValue >> 8);
    byteArray[size++] = (byte) intValue;
    
    return this;
}

private void resize(int newCapacity) {
    byte[] newArray = new byte[newCapacity];
    System.arraycopy(byteArray, 0, newArray, 0, size);
    byteArray = newArray;
}
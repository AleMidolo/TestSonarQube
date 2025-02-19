final ByteVector put11(final int byteValue1, final int byteValue2) {
    if (byteValue1 < Byte.MIN_VALUE || byteValue1 > Byte.MAX_VALUE || 
        byteValue2 < Byte.MIN_VALUE || byteValue2 > Byte.MAX_VALUE) {
        throw new IllegalArgumentException("Values must be between -128 and 127.");
    }
    
    if (size + 2 > capacity) {
        resize();
    }
    
    byteArray[size++] = (byte) byteValue1;
    byteArray[size++] = (byte) byteValue2;
    
    return this;
}

private void resize() {
    int newCapacity = capacity * 2;
    byte[] newArray = new byte[newCapacity];
    System.arraycopy(byteArray, 0, newArray, 0, size);
    byteArray = newArray;
    capacity = newCapacity;
}
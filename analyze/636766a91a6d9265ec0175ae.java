public ByteVector putByteArray(final byte[] byteArrayValue, final int byteOffset, final int byteLength) {
    if (byteArrayValue == null) {
        byteArrayValue = new byte[byteLength];
    } else if (byteOffset < 0 || byteLength < 0 || byteOffset + byteLength > byteArrayValue.length) {
        throw new IndexOutOfBoundsException("Invalid byteOffset or byteLength");
    }

    int newSize = this.size + byteLength;
    ensureCapacity(newSize);

    System.arraycopy(byteArrayValue, byteOffset, this.data, this.size, byteLength);
    this.size = newSize;

    return this;
}

private void ensureCapacity(int minCapacity) {
    if (minCapacity - this.data.length > 0) {
        int newCapacity = Math.max(this.data.length * 2, minCapacity);
        this.data = Arrays.copyOf(this.data, newCapacity);
    }
}
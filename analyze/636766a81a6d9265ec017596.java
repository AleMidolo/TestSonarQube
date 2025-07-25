import java.util.Arrays;

public class ByteVector {
    private byte[] data;
    private int size;

    public ByteVector() {
        this.data = new byte[10]; // Initial capacity
        this.size = 0;
    }

    /** 
     * Inserisce un intero in questo vettore di byte. Il vettore di byte viene automaticamente ingrandito se necessario.
     * @param intValue un intero.
     * @return questo vettore di byte.
     */
    public ByteVector putInt(final int intValue) {
        ensureCapacity(size + 4); // An integer takes 4 bytes
        data[size++] = (byte) (intValue >> 24);
        data[size++] = (byte) (intValue >> 16);
        data[size++] = (byte) (intValue >> 8);
        data[size++] = (byte) intValue;
        return this;
    }

    private void ensureCapacity(int minCapacity) {
        if (minCapacity - data.length > 0) {
            int newCapacity = Math.max(data.length * 2, minCapacity);
            data = Arrays.copyOf(data, newCapacity);
        }
    }

    public byte[] getData() {
        return Arrays.copyOf(data, size); // Return only the used portion of the array
    }
}
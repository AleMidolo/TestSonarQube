import java.io.IOException;

public class ClassReader {
    private byte[] data;

    public ClassReader(byte[] data) {
        this.data = data;
    }

    /**
     * Legge un valore long firmato in questo {@link ClassReader}. <i>Questo metodo è destinato alle sottoclassi di {@link Attribute} e normalmente non è necessario per i generatori di classi o adattatori.</i>
     * @param offset l'offset di partenza del valore da leggere in questo {@link ClassReader}.
     * @return il valore letto.
     */
    public long readLong(final int offset) {
        if (offset < 0 || offset + 8 > data.length) {
            throw new IndexOutOfBoundsException("Offset is out of bounds");
        }
        return ((long) (data[offset] & 0xFF) << 56) |
               ((long) (data[offset + 1] & 0xFF) << 48) |
               ((long) (data[offset + 2] & 0xFF) << 40) |
               ((long) (data[offset + 3] & 0xFF) << 32) |
               ((long) (data[offset + 4] & 0xFF) << 24) |
               ((long) (data[offset + 5] & 0xFF) << 16) |
               ((long) (data[offset + 6] & 0xFF) << 8) |
               ((long) (data[offset + 7] & 0xFF));
    }
}
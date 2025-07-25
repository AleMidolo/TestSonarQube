import java.io.ByteArrayOutputStream;
import java.io.IOException;

public final class Buffer {
    private ByteArrayOutputStream outputStream;

    public Buffer() {
        outputStream = new ByteArrayOutputStream();
    }

    public void write(byte[] data) throws IOException {
        outputStream.write(data);
    }

    /**
     * Restituisce un singolo array di byte contenente tutti i contenuti scritti nel/i buffer.
     */
    public final byte[] toByteArray() {
        return outputStream.toByteArray();
    }
}
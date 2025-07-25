import java.io.IOException;
import java.io.InputStream;

public class ByteReader {
    private InputStream buffer;
    private byte[] byteBuffer;
    private int currentIndex;
    private int bytesRead;

    public ByteReader(InputStream buffer) {
        this.buffer = buffer;
        this.byteBuffer = new byte[1024]; // Buffer size can be adjusted
        this.currentIndex = 0;
        this.bytesRead = 0;
    }

    /** 
     * Legge un byte dal <code>buffer</code> e lo riempie nuovamente se necessario.
     * @return Il prossimo byte dallo stream di input.
     * @throws IOException se non ci sono più dati disponibili.
     */
    public byte readByte() throws IOException {
        if (currentIndex >= bytesRead) {
            bytesRead = buffer.read(byteBuffer);
            currentIndex = 0;
            if (bytesRead == -1) {
                throw new IOException("No more data available.");
            }
        }
        return byteBuffer[currentIndex++];
    }
}
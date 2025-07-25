import java.io.IOException;
import java.io.InputStream;

public class VarintReader {
    private InputStream input;

    public VarintReader(InputStream input) {
        this.input = input;
    }

    /** 
     * Leggi un Varint "raw" dallo stream.
     */
    public long readRawVarint64() throws IOException {
        long result = 0;
        int shift = 0;
        while (true) {
            int b = input.read();
            if (b == -1) {
                throw new IOException("End of stream reached before varint was fully read.");
            }
            result |= (long) (b & 0x7F) << shift;
            if ((b & 0x80) == 0) {
                return result;
            }
            shift += 7;
            if (shift >= 64) {
                throw new IOException("Varint is too long.");
            }
        }
    }
}
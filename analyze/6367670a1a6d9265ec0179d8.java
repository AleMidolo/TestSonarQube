import java.io.IOException;
import java.io.OutputStream;

public class CustomOutputStream extends OutputStream {
    
    @Override 
    public void write(final byte[] b) throws IOException {
        if (b == null) {
            throw new NullPointerException("Byte array cannot be null");
        }
        // Example implementation: write bytes to a hypothetical output
        for (byte value : b) {
            // Here you would write the byte to the actual output destination
            System.out.write(value);
        }
    }

    @Override
    public void write(int b) throws IOException {
        // Implement the write method for a single byte if needed
        System.out.write(b);
    }
}
import java.io.IOException;
import java.io.OutputStream;

public class CustomOutputStream extends OutputStream {
    @Override
    public void write(byte b[]) throws IOException {
        if (b == null) {
            throw new IOException("Byte array cannot be null");
        }
        // Here you would implement the logic to write the byte array to the output stream.
        // For demonstration purposes, we will just print the byte array length.
        System.out.println("Writing " + b.length + " bytes to the output stream.");
    }

    @Override
    public void write(int b) throws IOException {
        // Implement the method to write a single byte if needed
    }
}
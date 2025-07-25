import java.nio.charset.StandardCharsets;
import java.util.LinkedList;

public class UTF8Writer {

    /** 
     * Scrive i byte codificati in utf8 dalla stringa nel {@link LinkedBuffer}.
     */
    public static LinkedBuffer writeUTF8(final CharSequence str, final WriteSession session, final LinkedBuffer lb) {
        if (str == null || lb == null) {
            throw new IllegalArgumentException("Input string and LinkedBuffer cannot be null");
        }

        byte[] utf8Bytes = str.toString().getBytes(StandardCharsets.UTF_8);
        lb.addBytes(utf8Bytes);
        return lb;
    }

    public static class LinkedBuffer {
        private final LinkedList<byte[]> buffers = new LinkedList<>();

        public void addBytes(byte[] bytes) {
            buffers.add(bytes);
        }

        public LinkedList<byte[]> getBuffers() {
            return buffers;
        }
    }

    public static class WriteSession {
        // Implementation of WriteSession can be added here
    }

    public static void main(String[] args) {
        // Example usage
        WriteSession session = new WriteSession();
        LinkedBuffer lb = new LinkedBuffer();
        writeUTF8("Hello, World!", session, lb);
        
        // Print the stored bytes for verification
        for (byte[] buffer : lb.getBuffers()) {
            System.out.println(new String(buffer, StandardCharsets.UTF_8));
        }
    }
}
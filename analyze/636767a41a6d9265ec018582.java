import java.io.IOException;
import java.io.OutputStream;

public static <T> int writeDelimitedTo(OutputStream out, T message, Schema<T> schema, LinkedBuffer buffer) throws IOException {
    // Serialize the message to a byte array
    byte[] messageBytes = schema.encode(message, buffer);
    
    // Write the length of the message
    int length = messageBytes.length;
    out.write(intToByteArray(length));
    
    // Write the message itself
    out.write(messageBytes);
    
    return length;
}

private static byte[] intToByteArray(int value) {
    return new byte[] {
        (byte) (value >> 24),
        (byte) (value >> 16),
        (byte) (value >> 8),
        (byte) value
    };
}
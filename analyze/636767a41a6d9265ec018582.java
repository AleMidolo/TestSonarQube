import java.io.IOException;
import java.io.OutputStream;
import com.google.protobuf.Schema;
import com.google.protobuf.LinkedBuffer;

public class MessageSerializer {

    /** 
     * Serializza il {@code message}, precedendolo con la sua lunghezza, in un {@link OutputStream}.
     * @return la dimensione del messaggio
     */
    public static <T> int writeDelimitedTo(OutputStream out, T message, Schema<T> schema, LinkedBuffer buffer) throws IOException {
        // Serialize the message to a byte array
        byte[] messageBytes = schema.encode(message, buffer);
        
        // Get the length of the message
        int length = messageBytes.length;
        
        // Write the length as a varint
        writeVarint(out, length);
        
        // Write the message bytes to the output stream
        out.write(messageBytes);
        
        return length;
    }

    private static void writeVarint(OutputStream out, int value) throws IOException {
        while ((value & ~0x7F) != 0) {
            out.write((value & 0x7F) | 0x80);
            value >>>= 7;
        }
        out.write(value);
    }
}
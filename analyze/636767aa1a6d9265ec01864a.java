import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class ByteArrayExample {
    
    /**
     * Copia i byte in un {@code byte[]}.
     */
    public byte[] toByteArray() {
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        try {
            // Example data to write to the byte array
            String exampleData = "Hello, World!";
            byteArrayOutputStream.write(exampleData.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }
        return byteArrayOutputStream.toByteArray();
    }

    public static void main(String[] args) {
        ByteArrayExample example = new ByteArrayExample();
        byte[] byteArray = example.toByteArray();
        System.out.println(new String(byteArray));
    }
}
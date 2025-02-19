import java.io.DataOutput;
import java.io.IOException;

public static int writeTo(final DataOutput out, LinkedBuffer node) throws IOException {
    int totalSize = 0;
    while (node != null) {
        byte[] data = node.getData(); // Assuming LinkedBuffer has a method to get its data
        out.write(data);
        totalSize += data.length;
        node = node.getNext(); // Assuming LinkedBuffer has a method to get the next node
    }
    return totalSize;
}
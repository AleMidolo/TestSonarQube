import java.io.InputStream;
import java.util.Stack;

public class FileAdder {
    
    /**
     * Aggiungi i file specificati in ordine inverso.
     */
    private void addReverse(final InputStream[] files) {
        Stack<InputStream> stack = new Stack<>();
        
        // Push all files onto the stack
        for (InputStream file : files) {
            stack.push(file);
        }
        
        // Pop files from the stack to add them in reverse order
        while (!stack.isEmpty()) {
            InputStream fileToAdd = stack.pop();
            // Add the file (implementation depends on the context)
            addFile(fileToAdd);
        }
    }
    
    private void addFile(InputStream file) {
        // Implementation for adding the file goes here
        // For example, reading the file or processing it
    }
}
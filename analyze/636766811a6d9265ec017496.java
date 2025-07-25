import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

public class FileIterator {
    private File[] files;
    private int currentIndex;

    public FileIterator(File directory) {
        if (directory.isDirectory()) {
            this.files = directory.listFiles();
        } else {
            this.files = new File[0];
        }
        this.currentIndex = 0;
    }

    /** 
     * Restituisce il prossimo oggetto {@link java.io.File} oppure {@code null} se non ci sono più file disponibili.
     */
    public InputStream next() throws IOException {
        if (currentIndex < files.length) {
            File file = files[currentIndex++];
            return new FileInputStream(file);
        }
        return null;
    }
}
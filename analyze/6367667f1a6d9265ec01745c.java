import java.io.File;
import java.net.URL;
import java.net.MalformedURLException;
import java.util.Vector;

@SuppressWarnings("unchecked") 
public static void addToClassPath(Vector<URL> cpV, String dir) {
    File directory = new File(dir);
    if (!directory.exists() || !directory.isDirectory()) {
        throw new IllegalArgumentException("The provided directory does not exist or is not a directory: " + dir);
    }

    File[] files = directory.listFiles((d, name) -> name.endsWith(".jar"));
    if (files != null) {
        for (File file : files) {
            try {
                cpV.add(file.toURI().toURL());
            } catch (MalformedURLException e) {
                System.err.println("Malformed URL for file: " + file.getAbsolutePath());
            }
        }
    }
}
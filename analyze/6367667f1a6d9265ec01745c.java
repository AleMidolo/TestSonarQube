import java.io.File;
import java.net.URL;
import java.util.Vector;

@SuppressWarnings("unchecked") 
public static void addToClassPath(Vector<URL> cpV, String dir) {
    File directory = new File(dir);
    if (directory.exists() && directory.isDirectory()) {
        File[] files = directory.listFiles((d, name) -> name.endsWith(".jar"));
        if (files != null) {
            for (File file : files) {
                try {
                    cpV.add(file.toURI().toURL());
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    } else {
        System.out.println("Directory does not exist or is not a directory: " + dir);
    }
}
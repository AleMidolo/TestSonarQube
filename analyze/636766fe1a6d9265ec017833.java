import java.io.File;
import java.io.IOException;

public static void forceDeleteOnExit(File file) throws IOException {
    if (file == null) {
        throw new NullPointerException("Il file non deve essere null");
    }

    Runtime.getRuntime().addShutdownHook(new Thread(() -> {
        try {
            deleteRecursively(file);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }));
}

private static void deleteRecursively(File file) throws IOException {
    if (file.isDirectory()) {
        File[] files = file.listFiles();
        if (files != null) {
            for (File child : files) {
                deleteRecursively(child);
            }
        }
    }
    if (!file.delete()) {
        throw new IOException("Impossibile cancellare il file: " + file.getAbsolutePath());
    }
}
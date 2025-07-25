import java.nio.file.Path;
import java.nio.file.Paths;

public class PathUtil {
    /** 
     * Applica il percorso relativo fornito al percorso dato, assumendo la separazione standard delle cartelle Java (cioè i separatori "/").
     * @param path il percorso da cui partire (di solito un percorso di file completo)
     * @param relativePath il percorso relativo da applicare (rispetto al percorso di file completo sopra)
     * @return il percorso di file completo che risulta dall'applicazione del percorso relativo
     */
    public static String applyRelativePath(String path, String relativePath) {
        Path basePath = Paths.get(path);
        Path resolvedPath = basePath.resolveSibling(relativePath);
        return resolvedPath.toString();
    }

    public static void main(String[] args) {
        String path = "/home/user/documents/file.txt";
        String relativePath = "../images/picture.png";
        String result = applyRelativePath(path, relativePath);
        System.out.println(result); // Output: /home/user/images/picture.png
    }
}
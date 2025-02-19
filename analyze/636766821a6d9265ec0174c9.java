import java.io.File;

private static File[] classPath() {
    String classpath = System.getProperty("java.class.path");
    String[] paths = classpath.split(File.pathSeparator);
    File[] files = new File[paths.length];
    
    for (int i = 0; i < paths.length; i++) {
        files[i] = new File(paths[i]);
    }
    
    return files;
}
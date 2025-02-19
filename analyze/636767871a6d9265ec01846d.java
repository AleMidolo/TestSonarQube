import java.io.File;

public static void createConfigurationDirectory() {
    String userHome = System.getProperty("user.home");
    String directoryPath = userHome + File.separator + "lf5";
    File directory = new File(directoryPath);
    
    if (!directory.exists()) {
        boolean created = directory.mkdirs();
        if (created) {
            System.out.println("Directory created: " + directoryPath);
        } else {
            System.out.println("Failed to create directory: " + directoryPath);
        }
    } else {
        System.out.println("Directory already exists: " + directoryPath);
    }
}
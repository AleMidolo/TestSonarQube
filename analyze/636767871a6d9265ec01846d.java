import java.io.File;

public class ConfigurationDirectoryCreator {
    
    /** 
     * Crea la directory in cui verrà scritta la lista dei file MRU. La directory "lf5" viene creata nella directory Documenti e Impostazioni sui computer Windows 2000 e ovunque punti la variabile user.home su tutte le altre piattaforme.
     */
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

    public static void main(String[] args) {
        createConfigurationDirectory();
    }
}
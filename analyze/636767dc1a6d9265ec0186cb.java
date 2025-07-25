public class ConfigurationInitializer {

    public void init() {
        // Check the distribution path
        String distributionPath = System.getProperty("distribution.path");
        
        if (distributionPath == null || distributionPath.isEmpty()) {
            throw new IllegalArgumentException("Distribution path is not set.");
        }
        
        // Additional initialization logic can be added here
        System.out.println("Configuration initialized with distribution path: " + distributionPath);
    }

    public static void main(String[] args) {
        ConfigurationInitializer initializer = new ConfigurationInitializer();
        initializer.init();
    }
}
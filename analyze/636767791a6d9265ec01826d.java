import java.util.Properties;

public class VariableSubstitutor {

    /** 
     * Trova il valore corrispondente a <code>key</code> in <code>props</code>. Quindi esegui la sostituzione delle variabili sul valore trovato.
     */
    public static String findAndSubst(String key, Properties props) {
        String value = props.getProperty(key);
        if (value == null) {
            return null; // or throw an exception based on your needs
        }
        
        // Replace variables in the value
        for (String propKey : props.stringPropertyNames()) {
            String propValue = props.getProperty(propKey);
            value = value.replace("${" + propKey + "}", propValue);
        }
        
        return value;
    }

    public static void main(String[] args) {
        Properties props = new Properties();
        props.setProperty("name", "John");
        props.setProperty("greeting", "Hello, ${name}!");

        String result = findAndSubst("greeting", props);
        System.out.println(result); // Output: Hello, John!
    }
}
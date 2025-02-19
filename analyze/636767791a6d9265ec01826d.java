import java.util.Properties;

public static String findAndSubst(String key, Properties props) {
    String value = props.getProperty(key);
    if (value == null) {
        return null;
    }
    
    for (String propKey : props.stringPropertyNames()) {
        value = value.replace("${" + propKey + "}", props.getProperty(propKey));
    }
    
    return value;
}
import org.apache.commons.beanutils.BeanMap;
import java.util.Map;

public class BeanMapUtil {

    /** 
     * Inserisce tutte le proprietà scrivibili dal BeanMap fornito in questo BeanMap. Le proprietà di sola lettura e di sola scrittura verranno ignorate.
     * @param map  il BeanMap le cui proprietà devono essere inserite
     */
    public void putAllWriteable(BeanMap map) {
        if (map == null) {
            throw new IllegalArgumentException("The provided BeanMap cannot be null.");
        }

        for (Object property : map.keySet()) {
            if (isWritable(property, map)) {
                Object value = map.get(property);
                this.put(property, value);
            }
        }
    }

    private boolean isWritable(Object property, BeanMap map) {
        // Implement logic to check if the property is writable
        // This is a placeholder for actual writable check logic
        return true; // Assume all properties are writable for this example
    }

    private void put(Object property, Object value) {
        // Implement logic to put the property and value into this BeanMap
        // This is a placeholder for actual put logic
    }
}
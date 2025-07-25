import java.util.HashSet;
import java.util.Set;

public class ObjectRegistry {
    private static final Set<Object> registeredObjects = new HashSet<>();

    /** 
     * <p> Registra l'oggetto fornito. Utilizzato dai metodi di riflessione per evitare loop infiniti. </p>
     * @param value L'oggetto da registrare.
     */
    static void register(Object value) {
        if (value != null) {
            registeredObjects.add(value);
        }
    }
}
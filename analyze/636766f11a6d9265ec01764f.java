import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class BeanMap {
    private Map<String, Object> map;

    public BeanMap() {
        this.map = new HashMap<>();
    }

    /**
     * Restituisce i valori per il BeanMap.
     * @return valori per il BeanMap. La collezione restituita non è modificabile.
     */
    public Collection<Object> values() {
        return Collections.unmodifiableCollection(map.values());
    }
}
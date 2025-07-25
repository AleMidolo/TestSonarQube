import java.util.HashMap;
import java.util.Map;

public class MyMap<K, V> {
    private Map<K, V> map;

    public MyMap() {
        this.map = new HashMap<>();
    }

    /** 
     * Restituisce <code>true</code> se questa mappa contiene una mappatura per la chiave specificata.
     * @param key  la chiave da cercare
     * @return true se la mappa contiene la chiave
     */
    @Override 
    public boolean containsKey(final Object key) {
        return map.containsKey(key);
    }

    // Additional methods to add and remove entries for testing purposes
    public void put(K key, V value) {
        map.put(key, value);
    }

    public void remove(K key) {
        map.remove(key);
    }
}
import java.util.HashMap;
import java.util.Map;

public class ValueAccumulator {
    private Map<String, Long> storage;

    public ValueAccumulator() {
        storage = new HashMap<>();
    }

    /** 
     * Accumula il valore con il valore esistente nella stessa chiave fornita.
     */
    public void valueAccumulation(String key, Long value) {
        storage.put(key, storage.getOrDefault(key, 0L) + value);
    }

    public Long getValue(String key) {
        return storage.getOrDefault(key, 0L);
    }

    public static void main(String[] args) {
        ValueAccumulator accumulator = new ValueAccumulator();
        accumulator.valueAccumulation("a", 10L);
        accumulator.valueAccumulation("a", 5L);
        System.out.println(accumulator.getValue("a")); // Output: 15
    }
}
import java.util.HashMap;
import java.util.Map;

public class MetricsCache {

    private final Map<String, Integer> cache = new HashMap<>();

    /** 
     * Accetta i dati nella cache e li unisce con il valore esistente. Questo metodo non è thread-safe, si dovrebbe evitare di chiamarlo in concorrenza.
     * @param data da aggiungere potenzialmente.
     */
    @Override 
    public void accept(final METRICS data) {
        if (data != null) {
            // Assuming METRICS has a method getKey() to get the key and getValue() to get the value
            String key = data.getKey();
            Integer value = data.getValue();

            cache.merge(key, value, Integer::sum);
        }
    }

    // Assuming a METRICS class for demonstration purposes
    public static class METRICS {
        private final String key;
        private final Integer value;

        public METRICS(String key, Integer value) {
            this.key = key;
            this.value = value;
        }

        public String getKey() {
            return key;
        }

        public Integer getValue() {
            return value;
        }
    }
}
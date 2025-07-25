import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LowerBoundCalculator<K> {

    /** 
     * Trova un limite inferiore massimo per ogni chiave.
     * @param keys lista delle chiavi.
     * @return i limiti inferiori delle chiavi calcolati.
     */
    private List<Integer> computeLowerBounds(List<K> keys) {
        Map<K, Integer> lowerBoundsMap = new HashMap<>();
        List<Integer> lowerBounds = new ArrayList<>();

        for (K key : keys) {
            // Simuliamo il calcolo di un limite inferiore per ogni chiave
            int lowerBound = calculateLowerBound(key);
            lowerBoundsMap.put(key, lowerBound);
        }

        for (K key : keys) {
            lowerBounds.add(lowerBoundsMap.get(key));
        }

        return lowerBounds;
    }

    private int calculateLowerBound(K key) {
        // Logica per calcolare il limite inferiore per la chiave
        // Qui si può implementare la logica specifica per il calcolo
        return key.hashCode() % 100; // Esempio di calcolo
    }
}
import java.util.HashMap;
import java.util.Map;

public class Accumulatore {
    private Map<String, Long> mappa = new HashMap<>();

    /** 
     * Accumula il valore con il valore esistente nella stessa chiave fornita.
     */
    public void accumulazioneValore(String chiave, Long valore) {
        mappa.put(chiave, mappa.getOrDefault(chiave, 0L) + valore);
    }
}
import java.util.Collection;
import java.util.Iterator;

public class MatchFinder {
    
    /** 
     * Restituisce il primo elemento in '<code>candidates</code>' che è contenuto in '<code>source</code>'. Se nessun elemento in '<code>candidates</code>' è presente in '<code>source</code>', restituisce <code>null</code>. L'ordine di iterazione è specifico dell'implementazione di {@link Collection}.
     * @param source la Collection sorgente
     * @param candidates i candidati da cercare
     * @return il primo oggetto presente, oppure <code>null</code> se non trovato
     */
    public static Object findFirstMatch(Collection source, Collection candidates) {
        if (source == null || candidates == null) {
            return null;
        }
        
        for (Object candidate : candidates) {
            if (source.contains(candidate)) {
                return candidate;
            }
        }
        
        return null;
    }
}
import java.util.HashSet;
import java.util.Set;

public class SetIntersection {

    /** 
     * Metodo efficiente per calcolare l'intersezione tra due insiemi
     * @param set1 insieme $1$
     * @param set2 insieme $2$
     * @return intersezione dell'insieme $1$ e $2$
     */
    private Set<V> intersection(Set<V> set1, Set<V> set2) {
        Set<V> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);
        return intersection;
    }
}
import java.util.HashSet;

public class MySet {
    private HashSet<Integer> set;

    public MySet() {
        set = new HashSet<>();
    }

    /** 
     * Inserisce un valore nel "set". Restituisce true se il "set" non conteneva già l'elemento specificato. 
     */
    public boolean insert(int val) {
        return set.add(val);
    }
}
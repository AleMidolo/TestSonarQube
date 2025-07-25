import java.util.HashSet;

public class CustomSet {
    private HashSet<Integer> set;

    public CustomSet() {
        set = new HashSet<>();
    }

    /** 
     * Inserisce un valore nel "set". Restituisce true se il "set" non conteneva già l'elemento specificato. 
     */
    public boolean insert(int val) {
        return set.add(val);
    }

    public static void main(String[] args) {
        CustomSet customSet = new CustomSet();
        System.out.println(customSet.insert(5)); // true
        System.out.println(customSet.insert(5)); // false
    }
}
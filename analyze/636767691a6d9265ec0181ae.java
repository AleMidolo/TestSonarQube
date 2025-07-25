import java.util.Enumeration;
import java.util.Vector;

public class EnumerationToArray {

    /** 
     * Copia l'Enumeration fornita in un array di Stringhe. L'Enumeration deve contenere solo elementi di tipo String.
     * @param enumeration l'Enumeration da copiare
     * @return l'array di Stringhe (<code>null</code> se l'Enumeration passata era <code>null</code>)
     */
    public static String[] toStringArray(Enumeration<String> enumeration) {
        if (enumeration == null) {
            return null;
        }

        Vector<String> vector = new Vector<>();
        while (enumeration.hasMoreElements()) {
            vector.add(enumeration.nextElement());
        }

        return vector.toArray(new String[0]);
    }

    public static void main(String[] args) {
        // Example usage
        Vector<String> vector = new Vector<>();
        vector.add("Hello");
        vector.add("World");
        Enumeration<String> enumeration = vector.elements();
        
        String[] result = toStringArray(enumeration);
        for (String str : result) {
            System.out.println(str);
        }
    }
}
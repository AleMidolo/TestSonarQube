import java.util.Arrays;

public class ArrayUtils {

    /** 
     * Restituisce un nuovo array di Stringhe senza elementi null. Metodo interno utilizzato per normalizzare le liste di esclusione (array e collezioni). Si noti che {@link Arrays#sort(Object[])} genererà un {@link NullPointerException} se un elemento dell'array è <code>null</code>.
     * @param array L'array da controllare
     * @return L'array fornito o un nuovo array senza null.
     */
    static String[] toNoNullStringArray(Object[] array) {
        if (array == null) {
            return new String[0];
        }
        return Arrays.stream(array)
                     .filter(obj -> obj != null)
                     .map(Object::toString)
                     .toArray(String[]::new);
    }

    public static void main(String[] args) {
        Object[] inputArray = { "Hello", null, "World", null, "!" };
        String[] resultArray = toNoNullStringArray(inputArray);
        System.out.println(Arrays.toString(resultArray)); // Output: [Hello, World, !]
    }
}
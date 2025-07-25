import java.util.Arrays;

public class HashCodeUtil {
    /** 
     * Restituisce un codice hash basato sul contenuto dell'array specificato. Se <code>array</code> è <code>null</code>, questo metodo restituisce 0.
     * @param array l'array di long per ottenere un codice hash
     * @return il codice hash dell'array di long, che potrebbe essere 0 se l'array è null.
     */
    public static int nullSafeHashCode(long[] array) {
        if (array == null) {
            return 0;
        }
        return Arrays.hashCode(array);
    }

    public static void main(String[] args) {
        long[] array1 = {1L, 2L, 3L};
        long[] array2 = null;

        System.out.println(nullSafeHashCode(array1)); // Output: hash code of array1
        System.out.println(nullSafeHashCode(array2)); // Output: 0
    }
}
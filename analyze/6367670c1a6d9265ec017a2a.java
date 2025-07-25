import java.util.Objects;

public class ArrayConverter {

    /** 
     * <p>Converte un array di oggetti Integer in primitivi.</p> 
     * <p>Questo metodo restituisce <code>null</code> per un array di input <code>null</code>.</p>
     * @param array  un array di <code>Integer</code>, può essere <code>null</code>
     * @return un array di <code>int</code>, <code>null</code> se l'array di input è nullo
     * @throws NullPointerException se il contenuto dell'array è <code>null</code>
     */
    public static int[] toPrimitive(final Integer[] array) {
        if (array == null) {
            return null;
        }
        int[] result = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            if (array[i] == null) {
                throw new NullPointerException("Element at index " + i + " is null");
            }
            result[i] = array[i];
        }
        return result;
    }

    public static void main(String[] args) {
        Integer[] integerArray = {1, 2, 3, null};
        try {
            int[] primitiveArray = toPrimitive(integerArray);
        } catch (NullPointerException e) {
            System.out.println(e.getMessage());
        }
    }
}
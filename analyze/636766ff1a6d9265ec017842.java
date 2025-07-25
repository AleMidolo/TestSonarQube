import java.util.Objects;

public class ArrayConverter {

    /** 
     * <p>Converte un array di oggetti Double in primitivi.</p> 
     * <p>Questo metodo restituisce <code>null</code> per un array di input <code>null</code>.</p>
     * @param array  un array di <code>Double</code>, può essere <code>null</code>
     * @return un array di <code>double</code>, <code>null</code> se l'array di input è nullo
     * @throws NullPointerException se il contenuto dell'array è <code>null</code>
     */
    public static double[] toPrimitive(final Double[] array) {
        if (array == null) {
            return null;
        }
        double[] result = new double[array.length];
        for (int i = 0; i < array.length; i++) {
            if (array[i] == null) {
                throw new NullPointerException("Element at index " + i + " is null");
            }
            result[i] = array[i];
        }
        return result;
    }

    public static void main(String[] args) {
        Double[] doubleArray = {1.1, 2.2, 3.3};
        double[] primitiveArray = toPrimitive(doubleArray);
        for (double d : primitiveArray) {
            System.out.println(d);
        }
    }
}
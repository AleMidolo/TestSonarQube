import java.util.Objects;

public class ByteArrayConverter {

    /** 
     * <p>Converte un array di oggetti Byte in primitivi.</p> 
     * <p>Questo metodo restituisce <code>null</code> per un array di input <code>null</code>.</p>
     * @param array  un array di <code>Byte</code>, può essere <code>null</code>
     * @return un array di <code>byte</code>, <code>null</code> se l'array di input è nullo
     * @throws NullPointerException se il contenuto dell'array è <code>null</code>
     */
    public static byte[] toPrimitive(final Byte[] array) {
        if (array == null) {
            return null;
        }
        byte[] result = new byte[array.length];
        for (int i = 0; i < array.length; i++) {
            result[i] = Objects.requireNonNull(array[i], "Element at index " + i + " is null").byteValue();
        }
        return result;
    }

    public static void main(String[] args) {
        // Example usage
        Byte[] byteArray = {1, 2, 3, null}; // This will throw NullPointerException
        byte[] primitiveArray = toPrimitive(byteArray);
    }
}
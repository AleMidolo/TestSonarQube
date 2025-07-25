public class ArrayConverter {
    
    /** 
     * <p>Converte un array di short primitivi in oggetti.</p> <p>Questo metodo restituisce <code>null</code> per un array di input <code>null</code>.</p>
     * @param array  un array di <code>short</code>
     * @return un array di <code>Short</code>, <code>null</code> se l'array di input è nullo
     */
    public static Short[] toObject(final short[] array) {
        if (array == null) {
            return null;
        }
        Short[] result = new Short[array.length];
        for (int i = 0; i < array.length; i++) {
            result[i] = array[i]; // Autoboxing from short to Short
        }
        return result;
    }

    public static void main(String[] args) {
        short[] primitiveArray = {1, 2, 3, 4, 5};
        Short[] objectArray = toObject(primitiveArray);
        
        // Print the result
        for (Short s : objectArray) {
            System.out.println(s);
        }
    }
}
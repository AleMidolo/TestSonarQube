public class ArrayConverter {
    
    /** 
     * <p>Converte un array di int primitivi in oggetti.</p> <p>Questo metodo restituisce <code>null</code> per un array di input <code>null</code>.</p>
     * @param array  un array di <code>int</code>
     * @return un array di <code>Integer</code>, <code>null</code> se l'array di input è nullo
     */
    public static Integer[] toObject(final int[] array) {
        if (array == null) {
            return null;
        }
        
        Integer[] result = new Integer[array.length];
        for (int i = 0; i < array.length; i++) {
            result[i] = Integer.valueOf(array[i]);
        }
        return result;
    }

    public static void main(String[] args) {
        int[] primitiveArray = {1, 2, 3, 4, 5};
        Integer[] objectArray = toObject(primitiveArray);
        
        // Print the result
        for (Integer num : objectArray) {
            System.out.println(num);
        }
    }
}
public class ArrayConverter {
    /** 
     * <p>Converte un array di double primitivi in oggetti.</p> <p>Questo metodo restituisce <code>null</code> per un array di input <code>null</code>.</p>
     * @param array  un array di <code>double</code>
     * @return un array di <code>Double</code>, <code>null</code> se l'array di input è null
     */
    public static Double[] toObject(final double[] array) {
        if (array == null) {
            return null;
        }
        Double[] objectArray = new Double[array.length];
        for (int i = 0; i < array.length; i++) {
            objectArray[i] = array[i]; // Autoboxing from double to Double
        }
        return objectArray;
    }

    public static void main(String[] args) {
        double[] primitiveArray = {1.0, 2.0, 3.0};
        Double[] objectArray = toObject(primitiveArray);
        for (Double d : objectArray) {
            System.out.println(d);
        }
    }
}
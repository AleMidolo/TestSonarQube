public class ArrayUtils {
    /** 
     * <p>Controlla se un array di double primitivi è vuoto o <code>null</code>.</p>
     * @param array  l'array da testare
     * @return <code>true</code> se l'array è vuoto o <code>null</code>
     * @since 2.1
     */
    public static boolean isEmpty(final double[] array) {
        return array == null || array.length == 0;
    }

    public static void main(String[] args) {
        double[] testArray1 = null;
        double[] testArray2 = {};
        double[] testArray3 = {1.0, 2.0, 3.0};

        System.out.println(isEmpty(testArray1)); // true
        System.out.println(isEmpty(testArray2)); // true
        System.out.println(isEmpty(testArray3)); // false
    }
}
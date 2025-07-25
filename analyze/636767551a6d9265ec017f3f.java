public class ArrayUtils {
    /** 
     * Scambia i due elementi agli indici specificati nell'array fornito.
     * @param <V> il tipo di elementi nell'array
     * @param arr l'array
     * @param i l'indice del primo elemento
     * @param j l'indice del secondo elemento
     */
    public static final <V> void swap(V[] arr, int i, int j) {
        if (arr == null) {
            throw new IllegalArgumentException("Array cannot be null");
        }
        if (i < 0 || i >= arr.length || j < 0 || j >= arr.length) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        V temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        Integer[] array = {1, 2, 3, 4, 5};
        swap(array, 1, 3);
        for (Integer num : array) {
            System.out.print(num + " ");
        }
    }
}
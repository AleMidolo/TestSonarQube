public class ArrayCloner {
    
    /** 
     * <p>Clona un array restituendo un risultato di tipo cast e gestendo <code>null</code>.</p> 
     * <p>Questo metodo restituisce <code>null</code> per un array di input <code>null</code>.</p>
     * @param array  l'array da clonare, può essere <code>null</code>
     * @return l'array clonato, <code>null</code> se l'input è <code>null</code>
     */
    public static char[] clone(final char[] array) {
        if (array == null) {
            return null;
        }
        char[] clonedArray = new char[array.length];
        System.arraycopy(array, 0, clonedArray, 0, array.length);
        return clonedArray;
    }

    public static void main(String[] args) {
        char[] original = {'a', 'b', 'c'};
        char[] cloned = clone(original);
        
        // Print the cloned array
        if (cloned != null) {
            for (char c : cloned) {
                System.out.print(c + " ");
            }
        } else {
            System.out.println("Cloned array is null.");
        }
    }
}
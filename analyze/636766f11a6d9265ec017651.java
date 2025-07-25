public class ArrayUtil {

    private static final Character[] EMPTY_ARRAY = new Character[0];

    /** 
     * <p>Tecnica di programmazione difensiva per cambiare un riferimento <code>null</code> in uno vuoto.</p> 
     * <p>Questo metodo restituisce un array vuoto per un array di input <code>null</code>.</p> 
     * <p>Come tecnica di ottimizzazione della memoria, un array vuoto passato verrà sovrascritto con i riferimenti vuoti <code>public static</code> in questa classe.</p>
     * @param array  l'array da controllare per <code>null</code> o vuoto
     * @return lo stesso array, array vuoto <code>public static</code> se l'input è <code>null</code> o vuoto
     * @since 2.5
     */
    public static Character[] nullToEmpty(final Character[] array) {
        return (array == null || array.length == 0) ? EMPTY_ARRAY : array;
    }

    public static void main(String[] args) {
        Character[] nullArray = null;
        Character[] emptyArray = {};
        Character[] filledArray = { 'a', 'b', 'c' };

        System.out.println(nullToEmpty(nullArray)); // Should print: []
        System.out.println(nullToEmpty(emptyArray)); // Should print: []
        System.out.println(nullToEmpty(filledArray)); // Should print: [a, b, c]
    }
}
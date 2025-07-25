public class StringArrayTrimmer {
    
    /** 
     * Rimuove gli spazi bianchi dagli elementi dell'array di Stringhe fornito, chiamando <code>String.trim()</code> su ciascuno di essi.
     * @param array l'array di Stringhe originale
     * @return l'array risultante (della stessa dimensione) con elementi privati degli spazi bianchi
     */
    public static String[] trimArrayElements(String[] array) {
        if (array == null) {
            return null;
        }
        
        String[] trimmedArray = new String[array.length];
        for (int i = 0; i < array.length; i++) {
            trimmedArray[i] = array[i] != null ? array[i].trim() : null;
        }
        return trimmedArray;
    }

    public static void main(String[] args) {
        String[] originalArray = {"  Hello  ", "  World  ", null, "  Java  "};
        String[] trimmedArray = trimArrayElements(originalArray);
        
        for (String str : trimmedArray) {
            System.out.println("'" + str + "'");
        }
    }
}
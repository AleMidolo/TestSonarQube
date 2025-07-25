public class FileSeparatorIndex {

    /** 
     * Restituisce l'indice dell'ultimo carattere separatore di directory. <p> Questo metodo gestirà un file sia in formato Unix che Windows. Viene restituita la posizione dell'ultimo slash o backslash. <p> L'output sarà lo stesso indipendentemente dalla macchina su cui il codice viene eseguito.
     * @param filename  il nome del file in cui trovare l'ultimo separatore di percorso, null restituisce -1
     * @return l'indice dell'ultimo carattere separatore, oppure -1 se non esiste tale carattere
     */
    public static int indexOfLastSeparator(String filename) {
        if (filename == null) {
            return -1;
        }
        
        int lastSlashIndex = filename.lastIndexOf('/');
        int lastBackslashIndex = filename.lastIndexOf('\\');
        
        return Math.max(lastSlashIndex, lastBackslashIndex);
    }

    public static void main(String[] args) {
        // Test examples
        System.out.println(indexOfLastSeparator("C:\\Users\\Example\\file.txt")); // Output: 15
        System.out.println(indexOfLastSeparator("/home/user/example/file.txt")); // Output: 16
        System.out.println(indexOfLastSeparator("file.txt")); // Output: -1
        System.out.println(indexOfLastSeparator(null)); // Output: -1
    }
}
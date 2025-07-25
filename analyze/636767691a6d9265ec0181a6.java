public class StringSplitter {
    
    /** 
     * Divide una Stringa alla prima occorrenza del delimitatore. Non include il delimitatore nel risultato.
     * @param toSplit la stringa da dividere
     * @param delimiter il delimitatore con cui dividere la stringa
     * @return un array di due elementi con l'indice 0 che rappresenta la parte prima del delimitatore, e l'indice 1 che rappresenta la parte dopo il delimitatore (nessun elemento include il delimitatore); oppure <code>null</code> se il delimitatore non è stato trovato nella Stringa di input fornita
     */
    public static String[] split(String toSplit, String delimiter) {
        if (toSplit == null || delimiter == null) {
            return null;
        }
        
        int index = toSplit.indexOf(delimiter);
        if (index == -1) {
            return null;
        }
        
        String beforeDelimiter = toSplit.substring(0, index);
        String afterDelimiter = toSplit.substring(index + delimiter.length());
        
        return new String[] { beforeDelimiter, afterDelimiter };
    }

    public static void main(String[] args) {
        String[] result = split("Hello,World", ",");
        if (result != null) {
            System.out.println("Before: " + result[0]);
            System.out.println("After: " + result[1]);
        } else {
            System.out.println("Delimiter not found.");
        }
    }
}
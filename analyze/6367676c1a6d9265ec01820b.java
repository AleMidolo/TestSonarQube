public class StringManipulator {

    /** 
     * Elimina qualsiasi carattere in una Stringa data.
     * @param inString la Stringa originale
     * @param charsToDelete un insieme di caratteri da eliminare. Ad esempio, "az\n" eliminerà le 'a', le 'z' e le nuove righe.
     * @return la Stringa risultante
     */
    public static String deleteAny(String inString, String charsToDelete) {
        if (inString == null || charsToDelete == null) {
            return inString; // Return original string if input is null
        }
        
        StringBuilder result = new StringBuilder();
        for (char c : inString.toCharArray()) {
            if (charsToDelete.indexOf(c) == -1) {
                result.append(c); // Append character if it's not in charsToDelete
            }
        }
        return result.toString(); // Return the resulting string
    }

    public static void main(String[] args) {
        String original = "Hello World!";
        String charsToRemove = "lo";
        String result = deleteAny(original, charsToRemove);
        System.out.println(result); // Output: "He Wr!"
    }
}
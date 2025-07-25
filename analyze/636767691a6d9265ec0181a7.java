public class StringCleaner {
    
    /** 
     * Rimuove tutte le occorrenze del carattere iniziale fornito dalla Stringa data.
     * @param str la Stringa da controllare
     * @param leadingCharacter il carattere iniziale da rimuovere
     * @return la Stringa ripulita
     */
    public static String trimLeadingCharacter(String str, char leadingCharacter) {
        if (str == null || str.isEmpty()) {
            return str;
        }
        
        StringBuilder result = new StringBuilder();
        boolean leadingCharFound = false;

        for (char c : str.toCharArray()) {
            if (c == leadingCharacter) {
                leadingCharFound = true;
            } else {
                if (leadingCharFound) {
                    result.append(c);
                } else {
                    result.append(c);
                }
            }
        }
        
        return result.toString();
    }

    public static void main(String[] args) {
        String testString = "aaabacadae";
        char leadingChar = 'a';
        String cleanedString = trimLeadingCharacter(testString, leadingChar);
        System.out.println(cleanedString); // Output: "bcde"
    }
}
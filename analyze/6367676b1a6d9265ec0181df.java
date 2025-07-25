public class StringUtil {
    
    /** 
     * Restituisce {@code true} se la stringa fornita inizia con il prefisso specificato, ignorando le maiuscole, {@code false} altrimenti.
     * @param str la String da controllare
     * @param prefix il prefisso da cercare
     * @return {@code true} se la stringa fornita inizia con il prefisso specificato, ignorando le maiuscole, {@code false} altrimenti.
     * @see java.lang.String#startsWith
     */
    public static boolean startsWithIgnoreCase(String str, String prefix) {
        if (str == null || prefix == null) {
            return false;
        }
        return str.toLowerCase().startsWith(prefix.toLowerCase());
    }

    public static void main(String[] args) {
        System.out.println(startsWithIgnoreCase("Hello World", "hello")); // true
        System.out.println(startsWithIgnoreCase("Hello World", "world")); // false
        System.out.println(startsWithIgnoreCase("Hello World", null)); // false
        System.out.println(startsWithIgnoreCase(null, "hello")); // false
    }
}
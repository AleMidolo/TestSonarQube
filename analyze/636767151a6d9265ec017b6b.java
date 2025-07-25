public class StringUtil {

    /** 
     * <p>Controlla se una Stringa inizia con un prefisso specificato (opzionalmente senza distinzione tra maiuscole e minuscole).</p>
     * @see String#startsWith(String)
     * @param str  la Stringa da controllare, può essere null
     * @param prefix il prefisso da trovare, può essere null
     * @param ignoreCase indica se il confronto deve ignorare le maiuscole e minuscole (senza distinzione tra maiuscole e minuscole) o meno.
     * @return <code>true</code> se la Stringa inizia con il prefisso o entrambi <code>null</code>
     */
    private static boolean startsWith(final String str, final String prefix, final boolean ignoreCase) {
        if (str == null && prefix == null) {
            return true;
        }
        if (str == null || prefix == null) {
            return false;
        }
        if (ignoreCase) {
            return str.toLowerCase().startsWith(prefix.toLowerCase());
        } else {
            return str.startsWith(prefix);
        }
    }

    public static void main(String[] args) {
        System.out.println(startsWith("Hello World", "Hello", false)); // true
        System.out.println(startsWith("Hello World", "hello", true));  // true
        System.out.println(startsWith("Hello World", "World", false)); // false
        System.out.println(startsWith(null, null, false));              // true
        System.out.println(startsWith(null, "Hello", false));          // false
    }
}
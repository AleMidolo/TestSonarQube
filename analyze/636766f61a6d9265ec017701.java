public class StringUtil {
    
    /** 
     * Trova l'ultimo indice all'interno di una Stringa, gestendo <code>null</code>. Questo metodo utilizza {@link String#lastIndexOf(String)}. 
     */
    public static int lastIndexOf(String str, String searchStr) {
        if (str == null || searchStr == null) {
            return -1;
        }
        return str.lastIndexOf(searchStr);
    }

    public static void main(String[] args) {
        // Test cases
        System.out.println(lastIndexOf("Hello World", "o")); // Output: 7
        System.out.println(lastIndexOf("Hello World", "l")); // Output: 9
        System.out.println(lastIndexOf("Hello World", "x")); // Output: -1
        System.out.println(lastIndexOf(null, "o")); // Output: -1
        System.out.println(lastIndexOf("Hello World", null)); // Output: -1
    }
}
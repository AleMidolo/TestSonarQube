public class StringIndexFinder {
    
    /** 
     * Trova il primo indice all'interno di una Stringa, gestendo <code>null</code>. Questo metodo utilizza {@link String#indexOf(String)}. 
     */
    public static int indexOf(String str, String searchStr) {
        if (str == null || searchStr == null) {
            return -1;
        }
        return str.indexOf(searchStr);
    }

    public static void main(String[] args) {
        // Test cases
        System.out.println(indexOf("Hello, world!", "world")); // Output: 7
        System.out.println(indexOf("Hello, world!", "Java"));  // Output: -1
        System.out.println(indexOf(null, "test"));              // Output: -1
        System.out.println(indexOf("test", null));              // Output: -1
    }
}
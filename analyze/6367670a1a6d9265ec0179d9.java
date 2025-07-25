public class StringUtil {
    /** 
     * Ottiene la lunghezza di una Stringa o <code>0</code> se la Stringa è <code>null</code>.
     * @param str una Stringa o <code>null</code>
     * @return lunghezza della Stringa o <code>0</code> se la Stringa è <code>null</code>.
     * @since 2.4
     */
    public static int length(final String str) {
        return str == null ? 0 : str.length();
    }

    public static void main(String[] args) {
        System.out.println(length("Hello")); // Output: 5
        System.out.println(length(null));     // Output: 0
    }
}
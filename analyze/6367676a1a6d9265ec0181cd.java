public class StringUtil {
    
    /** 
     * Rimuove gli spazi bianchi iniziali dalla Stringa fornita.
     * @param str la Stringa da controllare
     * @return la Stringa senza spazi bianchi iniziali
     * @see java.lang.Character#isWhitespace
     */
    public static String trimLeadingWhitespace(String str) {
        if (str == null) {
            return null;
        }
        int index = 0;
        while (index < str.length() && Character.isWhitespace(str.charAt(index))) {
            index++;
        }
        return str.substring(index);
    }

    public static void main(String[] args) {
        String testString = "   Hello World!";
        String result = trimLeadingWhitespace(testString);
        System.out.println("'" + result + "'"); // Output: 'Hello World!'
    }
}
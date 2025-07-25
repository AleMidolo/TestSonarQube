public class CharUtils {
    /** 
     * <p>Controlla se il carattere è un carattere alfabetico maiuscolo ASCII a 7 bit.</p> 
     * <pre> 
     * CharUtils.isAsciiAlphaUpper('a')  = false 
     * CharUtils.isAsciiAlphaUpper('A')  = true 
     * CharUtils.isAsciiAlphaUpper('3')  = false 
     * CharUtils.isAsciiAlphaUpper('-')  = false 
     * CharUtils.isAsciiAlphaUpper('\n') = false 
     * CharUtils.isAsciiAlphaUpper('&copy;') = false 
     * </pre>
     * @param ch  il carattere da controllare
     * @return true se compreso tra 65 e 90 inclusi
     */
    public static boolean isAsciiAlphaUpper(final char ch) {
        return ch >= 65 && ch <= 90;
    }

    public static void main(String[] args) {
        System.out.println(isAsciiAlphaUpper('a')); // false
        System.out.println(isAsciiAlphaUpper('A')); // true
        System.out.println(isAsciiAlphaUpper('3')); // false
        System.out.println(isAsciiAlphaUpper('-')); // false
        System.out.println(isAsciiAlphaUpper('\n')); // false
        System.out.println(isAsciiAlphaUpper('&')); // false
    }
}
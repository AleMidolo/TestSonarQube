public class CharUtils {
    /** 
     * <p>Converte il Character in un char gestendo <code>null</code>.</p> 
     * <pre> 
     * CharUtils.toChar(null, 'X') = 'X' 
     * CharUtils.toChar(' ', 'X')  = ' ' 
     * CharUtils.toChar('A', 'X')  = 'A' 
     * </pre>
     * @param ch  il carattere da convertire
     * @param defaultValue  il valore da utilizzare se il Character è null
     * @return il valore char del Character o il valore predefinito se null
     */
    public static char toChar(final Character ch, final char defaultValue) {
        return (ch != null) ? ch : defaultValue;
    }

    public static void main(String[] args) {
        System.out.println(toChar(null, 'X')); // Output: X
        System.out.println(toChar(' ', 'X'));  // Output:  
        System.out.println(toChar('A', 'X'));  // Output: A
    }
}
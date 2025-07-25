public class HexConverter {
    
    /** 
     * @param b Un carattere codificato in ASCII da 0-9, a-f, A-F
     * @return Il valore byte del carattere da 0 a 16.
     */
    public static byte convertHexDigit(byte b) {
        if (b >= '0' && b <= '9') {
            return (byte) (b - '0');
        } else if (b >= 'a' && b <= 'f') {
            return (byte) (b - 'a' + 10);
        } else if (b >= 'A' && b <= 'F') {
            return (byte) (b - 'A' + 10);
        } else {
            throw new IllegalArgumentException("Input must be a hex digit (0-9, a-f, A-F)");
        }
    }

    public static void main(String[] args) {
        // Test the function
        System.out.println(convertHexDigit((byte) '0')); // Output: 0
        System.out.println(convertHexDigit((byte) '9')); // Output: 9
        System.out.println(convertHexDigit((byte) 'a')); // Output: 10
        System.out.println(convertHexDigit((byte) 'f')); // Output: 15
        System.out.println(convertHexDigit((byte) 'A')); // Output: 10
        System.out.println(convertHexDigit((byte) 'F')); // Output: 15
    }
}
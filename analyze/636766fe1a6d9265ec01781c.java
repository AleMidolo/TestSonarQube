public class CharUtils {
    private static final Character[] cache = new Character[128];

    static {
        for (int i = 0; i < cache.length; i++) {
            cache[i] = (char) i;
        }
    }

    /**
     * <p>Converte il carattere in un oggetto Character.</p>
     * <p>Per i caratteri ASCII a 7 bit, utilizza una cache che restituirà lo stesso oggetto Character ogni volta.</p>
     * <pre> CharUtils.toCharacterObject(' ')  = ' ' CharUtils.toCharacterObject('A')  = 'A' </pre>
     * @param ch  il carattere da convertire
     * @return un oggetto Character del carattere specificato
     */
    public static Character toCharacterObject(final char ch) {
        if (ch >= 0 && ch < 128) {
            return cache[ch];
        }
        return Character.valueOf(ch);
    }

    public static void main(String[] args) {
        System.out.println(toCharacterObject(' ')); // Output: ' '
        System.out.println(toCharacterObject('A')); // Output: 'A'
        System.out.println(toCharacterObject('ñ')); // Output: 'ñ'
    }
}
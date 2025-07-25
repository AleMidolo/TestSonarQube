public class SubstringMatcher {

    /** 
     * Restituisce {@code true} se la stringa fornita corrisponde alla sottostringa fornita all'indice specificato, {@code false} altrimenti.
     * @param str la stringa originale (o StringBuilder)
     * @param index l'indice nella stringa originale da cui iniziare a confrontare
     * @param substring la sottostringa da confrontare all'indice specificato
     * @return {@code true} se la stringa fornita corrisponde alla sottostringa fornita all'indice specificato, {@code false} altrimenti.
     */
    public static boolean substringMatch(CharSequence str, int index, CharSequence substring) {
        if (str == null || substring == null) {
            return false;
        }
        if (index < 0 || index + substring.length() > str.length()) {
            return false;
        }
        for (int i = 0; i < substring.length(); i++) {
            if (str.charAt(index + i) != substring.charAt(i)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        // Test examples
        System.out.println(substringMatch("Hello, World!", 7, "World")); // true
        System.out.println(substringMatch("Hello, World!", 7, "world")); // false
        System.out.println(substringMatch("Hello, World!", 0, "Hello")); // true
        System.out.println(substringMatch("Hello, World!", 5, ", W")); // true
        System.out.println(substringMatch("Hello, World!", 12, "!")); // true
        System.out.println(substringMatch("Hello, World!", 13, "!")); // false
    }
}
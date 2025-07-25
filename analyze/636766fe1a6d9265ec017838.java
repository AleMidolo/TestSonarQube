public class CharacterArrayConverter {

    /** 
     * <p>Converte un array di oggetti Character in primitivi.</p> 
     * <p>Questo metodo restituisce <code>null</code> per un array di input <code>null</code>.</p>
     * @param array  un array di <code>Character</code>, può essere <code>null</code>
     * @return un array di <code>char</code>, <code>null</code> se l'array di input è null
     * @throws NullPointerException se il contenuto dell'array è <code>null</code>
     */
    public static char[] toPrimitive(final Character[] array) {
        if (array == null) {
            return null;
        }
        
        char[] result = new char[array.length];
        for (int i = 0; i < array.length; i++) {
            if (array[i] == null) {
                throw new NullPointerException("Element at index " + i + " is null");
            }
            result[i] = array[i];
        }
        return result;
    }

    public static void main(String[] args) {
        Character[] charArray = { 'a', 'b', 'c' };
        char[] primitiveArray = toPrimitive(charArray);
        for (char c : primitiveArray) {
            System.out.print(c + " ");
        }
    }
}
public class SubstringCounter {

    /** 
     * Restituisce il numero di occorrenze della sottostringa {@code sub} nella stringa {@code str}.
     * @param str stringa in cui cercare. Restituisce 0 se è null.
     * @param sub stringa da cercare. Restituisce 0 se è null.
     * @return il numero di occorrenze della sottostringa {@code sub} nella stringa {@code str}.
     */
    public static int countOccurrencesOf(String str, String sub) {
        if (str == null || sub == null) {
            return 0;
        }
        
        int count = 0;
        int index = 0;
        
        while ((index = str.indexOf(sub, index)) != -1) {
            count++;
            index += sub.length();
        }
        
        return count;
    }

    public static void main(String[] args) {
        String str = "hello world, hello universe";
        String sub = "hello";
        System.out.println(countOccurrencesOf(str, sub)); // Output: 2
    }
}
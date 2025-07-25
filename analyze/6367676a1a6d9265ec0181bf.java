public class QuoteTransformer {

    /** 
     * Trasforma l'oggetto fornito in una Stringa con virgolette singole se è una Stringa;altrimenti, mantiene l'oggetto così com'è.
     * @param obj l'oggetto di input (ad esempio, "myString")
     * @return la Stringa quotata (ad esempio, "'myString'"), oppure l'oggetto di input così com'è se non è una Stringa
     */
    public static Object quoteIfString(Object obj) {
        if (obj instanceof String) {
            return "'" + obj + "'";
        }
        return obj;
    }

    public static void main(String[] args) {
        System.out.println(quoteIfString("myString")); // Output: 'myString'
        System.out.println(quoteIfString(123));        // Output: 123
        System.out.println(quoteIfString(null));       // Output: null
    }
}
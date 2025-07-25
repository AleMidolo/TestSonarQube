public class ObjectConverter {

    /** 
     * Conversione da 'Object' a stringa, se l'oggetto è nullo allora restituisce null, altrimenti restituisce toString(); 
     */
    public static String toString(Object object) {
        return object == null ? null : object.toString();
    }

    public static void main(String[] args) {
        Object obj1 = null;
        Object obj2 = new Object();
        System.out.println(toString(obj1)); // Output: null
        System.out.println(toString(obj2)); // Output: java.lang.Object@<hashcode>
    }
}
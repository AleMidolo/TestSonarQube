public class TemplateEncoder {

    /** 
     * Codifica una stringa con nomi di parametri di template presenti, in particolare i caratteri '{' e '}' verranno codificati in percentuale.
     * @param s la stringa con zero o più nomi di parametri di template
     * @return la stringa con i nomi di parametri di template codificati.
     */
    public static String encodeTemplateNames(String s) {
        if (s == null) {
            return null;
        }
        return s.replace("{", "%7B").replace("}", "%7D");
    }

    public static void main(String[] args) {
        String input = "Hello {name}, welcome to {place}!";
        String encoded = encodeTemplateNames(input);
        System.out.println(encoded); // Output: Hello %7Bname%7D, welcome to %7Bplace%7D!
    }
}
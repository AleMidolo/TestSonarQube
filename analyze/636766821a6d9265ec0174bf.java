import java.beans.Introspector;
import java.beans.PropertyDescriptor;

public class StringUtil {

    /** 
     * Inverso di Introspector.decapitalize
     */
    public static String capitalize(String name) {
        if (name == null || name.isEmpty()) {
            return name;
        }
        return Character.toUpperCase(name.charAt(0)) + name.substring(1);
    }

    public static void main(String[] args) {
        // Test the capitalize method
        System.out.println(capitalize("hello")); // Output: Hello
        System.out.println(capitalize("java"));   // Output: Java
        System.out.println(capitalize(""));       // Output: (empty string)
        System.out.println(capitalize(null));     // Output: null
    }
}
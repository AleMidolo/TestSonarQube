import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ArrayUtils {
    /** 
     * Array in Lista. <p> Funziona come {@link Arrays#asList(Object)}, ma gestisce gli array nulli.
     * @return una lista supportata dall'array.
     */
    public static <T> List<T> asList(T[] a) {
        if (a == null) {
            return Collections.emptyList();
        }
        return Arrays.asList(a);
    }

    public static void main(String[] args) {
        // Test the asList method
        String[] array = {"Hello", "World"};
        List<String> list = asList(array);
        System.out.println(list); // Output: [Hello, World]

        String[] nullArray = null;
        List<String> nullList = asList(nullArray);
        System.out.println(nullList); // Output: []
    }
}
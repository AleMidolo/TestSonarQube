import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public static <T> List<T> asList(T[] a) {
    return (a == null) ? Collections.emptyList() : Arrays.asList(a);
}
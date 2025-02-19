import java.util.Collection;

public static boolean containsInstance(Collection collection, Object element) {
    for (Object obj : collection) {
        if (obj == element) {
            return true;
        }
    }
    return false;
}
import java.util.Collection;

public static Object findFirstMatch(Collection source, Collection candidates) {
    for (Object candidate : candidates) {
        if (source.contains(candidate)) {
            return candidate;
        }
    }
    return null;
}
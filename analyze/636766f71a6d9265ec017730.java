import java.util.Collection;
import java.util.stream.Collectors;

public class CollectionConverter {
    
    /** 
     * Converte la Collection fornita in un array di Stringhe. L'array restituito non contiene elementi <code>null</code>. Si noti che {@link Arrays#sort(Object[])} genererà un {@link NullPointerException} se un elemento dell'array è <code>null</code>.
     * @param collection La collezione da convertire
     * @return Un nuovo array di Stringhe.
     */
    static String[] toNoNullStringArray(Collection<?> collection) {
        if (collection == null) {
            return new String[0];
        }
        return collection.stream()
                         .filter(item -> item != null)
                         .map(Object::toString)
                         .toArray(String[]::new);
    }
}
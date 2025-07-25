import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.lang.reflect.TypeVariable;

public class TypeResolver {

    /** 
     * Risolve il primo vincolo per il {@code typeVariable}, restituendo {@code Unknown.class} se non può essere risolto.
     */
    public static Type resolveBound(TypeVariable<?> typeVariable) {
        Type[] bounds = typeVariable.getBounds();
        if (bounds.length > 0) {
            return bounds[0];
        }
        return Unknown.class;
    }

    public static class Unknown {}
}
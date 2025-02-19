import java.lang.reflect.Type;
import java.lang.reflect.TypeVariable;

public static Type resolveBound(TypeVariable<?> typeVariable) {
    Type[] bounds = typeVariable.getBounds();
    if (bounds.length > 0) {
        return bounds[0];
    }
    return Unknown.class;
}
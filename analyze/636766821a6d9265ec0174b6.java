import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.Arrays;

public class TypeResolver {

    /** 
     * Risolve gli argomenti per il {@code genericType} utilizzando le informazioni sulle variabili di tipo per il {@code targetType}. Restituisce {@code null} se {@code genericType} non è parametrizzato o se gli argomenti non possono essere risolti.
     */
    public static Class<?>[] resolveArguments(Type genericType, Class<?> targetType) {
        if (!(genericType instanceof ParameterizedType)) {
            return null;
        }

        ParameterizedType parameterizedType = (ParameterizedType) genericType;
        Type[] actualTypeArguments = parameterizedType.getActualTypeArguments();
        Type rawType = parameterizedType.getRawType();

        if (rawType instanceof Class<?>) {
            Class<?> rawClass = (Class<?>) rawType;
            if (rawClass.isAssignableFrom(targetType)) {
                Class<?>[] resolvedArguments = new Class[actualTypeArguments.length];
                for (int i = 0; i < actualTypeArguments.length; i++) {
                    resolvedArguments[i] = (Class<?>) actualTypeArguments[i];
                }
                return resolvedArguments;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        // Example usage
        Type genericType = new ParameterizedTypeImpl(List.class, new Type[]{String.class});
        Class<?> targetType = List.class;

        Class<?>[] arguments = resolveArguments(genericType, targetType);
        System.out.println(Arrays.toString(arguments)); // Should print: [class java.lang.String]
    }
}

// A simple implementation of ParameterizedType for demonstration purposes
class ParameterizedTypeImpl implements ParameterizedType {
    private final Class<?> raw;
    private final Type[] actualTypeArguments;

    public ParameterizedTypeImpl(Class<?> raw, Type[] actualTypeArguments) {
        this.raw = raw;
        this.actualTypeArguments = actualTypeArguments;
    }

    @Override
    public Type[] getActualTypeArguments() {
        return actualTypeArguments;
    }

    @Override
    public Type getRawType() {
        return raw;
    }

    @Override
    public Type getOwnerType() {
        return null;
    }
}
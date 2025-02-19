import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;

public static Class<?>[] resolveArguments(Type genericType, Class<?> targetType) {
    if (!(genericType instanceof ParameterizedType)) {
        return null;
    }

    ParameterizedType parameterizedType = (ParameterizedType) genericType;
    Type[] actualTypeArguments = parameterizedType.getActualTypeArguments();
    Class<?>[] resolvedArguments = new Class[actualTypeArguments.length];

    for (int i = 0; i < actualTypeArguments.length; i++) {
        Type arg = actualTypeArguments[i];
        if (arg instanceof Class) {
            resolvedArguments[i] = (Class<?>) arg;
        } else if (arg instanceof ParameterizedType) {
            resolvedArguments[i] = (Class<?>) ((ParameterizedType) arg).getRawType();
        } else {
            return null; // Cannot resolve the argument
        }
    }

    return resolvedArguments;
}
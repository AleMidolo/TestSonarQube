private static Object copyArrayGrow1(final Object array, final Class<?> newArrayComponentType) {
    if (array == null) {
        return java.lang.reflect.Array.newInstance(newArrayComponentType, 1);
    }
    
    int length = java.lang.reflect.Array.getLength(array);
    Object newArray = java.lang.reflect.Array.newInstance(array.getClass().getComponentType(), length + 1);
    
    System.arraycopy(array, 0, newArray, 0, length);
    
    return newArray;
}
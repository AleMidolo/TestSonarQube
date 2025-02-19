static String[] toNoNullStringArray(Object[] array) {
    if (array == null) {
        return new String[0];
    }
    
    return Arrays.stream(array)
                 .filter(Objects::nonNull)
                 .map(Object::toString)
                 .toArray(String[]::new);
}
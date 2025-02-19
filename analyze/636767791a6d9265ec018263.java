private Class findClass(final String className) throws ClassNotFoundException {
    if (className == null) {
        throw new IllegalArgumentException("className cannot be null");
    }
    return Class.forName(className);
}
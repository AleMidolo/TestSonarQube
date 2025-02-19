static void register(Object value) {
    if (value == null) {
        return;
    }
    // Implement the registration logic here
    // For example, you might want to add the object to a Set to avoid duplicates
    Set<Object> registeredObjects = new HashSet<>();
    registeredObjects.add(value);
}
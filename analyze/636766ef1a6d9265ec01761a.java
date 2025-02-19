int addType(final String value) {
    // Assuming we have a list to store types
    List<String> types = new ArrayList<>();
    
    // Check if the type already exists
    int index = types.indexOf(value);
    if (index != -1) {
        // Type already exists, return the existing index
        return index;
    } else {
        // Add the new type and return the new index
        types.add(value);
        return types.size() - 1; // Return the index of the newly added type
    }
}
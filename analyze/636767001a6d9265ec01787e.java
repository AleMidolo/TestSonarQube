public String toString() {
    StringBuilder stringBuilder = new StringBuilder();
    // Assuming there are some components to append to the stringBuilder
    // For example, let's say we have a list of strings to concatenate
    List<String> components = getComponents(); // This method should return the components to be concatenated
    for (String component : components) {
        stringBuilder.append(component);
    }
    return stringBuilder.toString();
}
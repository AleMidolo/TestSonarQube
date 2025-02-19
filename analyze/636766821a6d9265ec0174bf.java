public static String capitalize(String name) {
    if (name == null || name.isEmpty()) {
        return name;
    }
    return Character.toUpperCase(name.charAt(0)) + name.substring(1);
}
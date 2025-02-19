public static String encodeTemplateNames(String s) {
    if (s == null) {
        return null;
    }
    return s.replace("{", "%7B").replace("}", "%7D");
}
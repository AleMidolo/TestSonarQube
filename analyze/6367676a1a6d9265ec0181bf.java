public static Object quoteIfString(Object obj) {
    if (obj instanceof String) {
        return "'" + obj + "'";
    }
    return obj;
}
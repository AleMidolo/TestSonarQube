public static String deleteAny(String inString, String charsToDelete) {
    StringBuilder result = new StringBuilder();
    for (char c : inString.toCharArray()) {
        if (charsToDelete.indexOf(c) == -1) {
            result.append(c);
        }
    }
    return result.toString();
}
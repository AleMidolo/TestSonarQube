public static String trimLeadingCharacter(String str, char leadingCharacter) {
    if (str == null) {
        return null;
    }
    
    StringBuilder result = new StringBuilder();
    for (char c : str.toCharArray()) {
        if (c != leadingCharacter) {
            result.append(c);
        }
    }
    
    return result.toString();
}
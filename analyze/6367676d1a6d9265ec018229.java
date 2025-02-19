public static String[] trimArrayElements(String[] array) {
    if (array == null) {
        return null;
    }
    
    String[] trimmedArray = new String[array.length];
    for (int i = 0; i < array.length; i++) {
        trimmedArray[i] = array[i] != null ? array[i].trim() : null;
    }
    return trimmedArray;
}
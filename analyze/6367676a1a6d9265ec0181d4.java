public static String[] addStringToArray(String[] array, String str) {
    int newSize = (array == null ? 0 : array.length) + 1;
    String[] newArray = new String[newSize];
    
    if (array != null) {
        System.arraycopy(array, 0, newArray, 0, array.length);
    }
    
    newArray[newSize - 1] = str;
    return newArray;
}
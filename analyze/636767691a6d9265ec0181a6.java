public static String[] split(String toSplit, String delimiter) {
    if (toSplit == null || delimiter == null) {
        return null;
    }
    
    int index = toSplit.indexOf(delimiter);
    if (index == -1) {
        return null;
    }
    
    String beforeDelimiter = toSplit.substring(0, index);
    String afterDelimiter = toSplit.substring(index + delimiter.length());
    
    return new String[] { beforeDelimiter, afterDelimiter };
}
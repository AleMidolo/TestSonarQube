public static int indexOfExtension(String filename) {
    if (filename == null) {
        return -1;
    }
    
    int lastDotIndex = filename.lastIndexOf('.');
    int lastSeparatorIndex = indexOfLastSeparator(filename);
    
    // Check if the last dot is after the last directory separator
    if (lastDotIndex > lastSeparatorIndex) {
        return lastDotIndex;
    }
    
    return -1;
}

private static int indexOfLastSeparator(String filename) {
    int lastUnixSeparator = filename.lastIndexOf('/');
    int lastWindowsSeparator = filename.lastIndexOf('\\');
    return Math.max(lastUnixSeparator, lastWindowsSeparator);
}
public static int indexOfLastSeparator(String filename) {
    if (filename == null) {
        return -1;
    }
    
    int lastUnixSeparator = filename.lastIndexOf('/');
    int lastWindowsSeparator = filename.lastIndexOf('\\');
    
    return Math.max(lastUnixSeparator, lastWindowsSeparator);
}
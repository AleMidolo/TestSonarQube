public static String stripFilenameExtension(String path) {
    if (path == null) {
        return null;
    }
    int lastDotIndex = path.lastIndexOf('.');
    int lastSlashIndex = Math.max(path.lastIndexOf('/'), path.lastIndexOf('\\'));
    
    if (lastDotIndex > lastSlashIndex) {
        return path.substring(0, lastDotIndex);
    }
    
    return path; // No extension found
}
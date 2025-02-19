public static String applyRelativePath(String path, String relativePath) {
    if (relativePath.startsWith("/")) {
        return relativePath;
    }
    
    String[] pathParts = path.split("/");
    String[] relativeParts = relativePath.split("/");
    
    int pathLength = pathParts.length;
    int relativeLength = relativeParts.length;
    
    if (relativeLength == 0) {
        return path;
    }
    
    // Remove the last part of the path if the relative path is not going up
    if (!relativePath.startsWith(".")) {
        pathLength--;
    }
    
    // Create a new array for the resulting path
    String[] resultParts = new String[pathLength + relativeLength];
    
    // Copy the base path parts
    System.arraycopy(pathParts, 0, resultParts, 0, pathLength);
    
    // Process the relative path
    for (String part : relativeParts) {
        if (part.equals("..")) {
            pathLength--;
        } else if (!part.equals(".")) {
            resultParts[pathLength++] = part;
        }
    }
    
    // Build the final path
    StringBuilder resultPath = new StringBuilder();
    for (int i = 0; i < pathLength; i++) {
        resultPath.append(resultParts[i]);
        if (i < pathLength - 1) {
            resultPath.append("/");
        }
    }
    
    return resultPath.toString();
}
private void addReverse(final InputStream[] files) {
    if (files == null || files.length == 0) {
        return;
    }
    
    for (int i = files.length - 1; i >= 0; i--) {
        InputStream file = files[i];
        // Logic to add the file
        // For example, you might want to read from the InputStream and process it
        // This is a placeholder for the actual file processing logic
        processFile(file);
    }
}

private void processFile(InputStream file) {
    // Implement the logic to process the InputStream
}
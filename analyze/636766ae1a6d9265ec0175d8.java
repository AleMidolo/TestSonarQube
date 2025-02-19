private String buildContentRange() {
    // Assuming we need to construct a Content-Range for a response
    long start = 0; // starting byte position
    long end = 100; // ending byte position
    long total = 500; // total size of the resource

    return String.format("bytes %d-%d/%d", start, end, total);
}
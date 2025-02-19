public Boolean isPartialContentResponse() {
    // Assuming we have a method to get the current HTTP response code
    int responseCode = getCurrentResponseCode();
    return responseCode == 206;
}

// Placeholder for the method to get the current HTTP response code
private int getCurrentResponseCode() {
    // This method should return the actual HTTP response code
    // For demonstration purposes, returning a dummy value
    return 200; // Replace with actual response code retrieval logic
}
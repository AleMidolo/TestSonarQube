private int parseEndOfLine(String headerPart, int end) {
    int index = headerPart.indexOf("\r\n", 0);
    if (index == -1 || index > end) {
        return end; // If no end of line found or it's beyond the end index, return end
    }
    return index; // Return the index of the end of line sequence
}
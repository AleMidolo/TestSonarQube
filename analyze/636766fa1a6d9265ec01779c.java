private String parseToken(final char[] terminators) {
    StringBuilder token = new StringBuilder();
    int ch;
    
    while ((ch = readNextCharacter()) != -1) {
        char currentChar = (char) ch;
        boolean isTerminator = false;

        for (char terminator : terminators) {
            if (currentChar == terminator) {
                isTerminator = true;
                break;
            }
        }

        if (isTerminator) {
            break;
        }

        token.append(currentChar);
    }

    return token.toString();
}

// This method is a placeholder for reading the next character from the input source.
private int readNextCharacter() {
    // Implementation for reading the next character goes here.
    return -1; // Placeholder return value
}
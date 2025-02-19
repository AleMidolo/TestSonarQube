private void pop(final int elements) {
    if (elements < 0) {
        throw new IllegalArgumentException("Number of elements to pop must be non-negative.");
    }
    for (int i = 0; i < elements; i++) {
        if (!outputStack.isEmpty()) {
            outputStack.pop();
        } else {
            break; // Stop if the stack is already empty
        }
    }
}
private int pop() {
    // Assuming there is a Stack<Integer> to hold the values
    if (outputFrameStack.isEmpty()) {
        throw new EmptyStackException(); // Handle empty stack case
    }
    return outputFrameStack.pop(); // Pop the top value from the stack
}
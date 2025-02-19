public static String peek() {
    // Assuming there's a Stack<String> to hold the diagnostic contexts
    if (ndcStack.isEmpty()) {
        return "";
    }
    return ndcStack.peek();
}
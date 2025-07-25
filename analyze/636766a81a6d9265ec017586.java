public class StackFrame {
    private final Stack<Object> stack;

    public StackFrame() {
        this.stack = new Stack<>();
    }

    /** 
     * Rimuove il numero specificato di tipi astratti dallo stack del frame di output.
     * @param elements il numero di tipi astratti che devono essere rimossi.
     */
    private void pop(final int elements) {
        if (elements < 0) {
            throw new IllegalArgumentException("Number of elements to pop must be non-negative.");
        }
        for (int i = 0; i < elements; i++) {
            if (!stack.isEmpty()) {
                stack.pop();
            } else {
                break; // Stop if the stack is already empty
            }
        }
    }

    // Method to push an element onto the stack for testing purposes
    public void push(Object element) {
        stack.push(element);
    }

    // Method to get the current size of the stack for testing purposes
    public int size() {
        return stack.size();
    }

    public static void main(String[] args) {
        StackFrame frame = new StackFrame();
        frame.push("Type1");
        frame.push("Type2");
        frame.push("Type3");
        
        System.out.println("Stack size before pop: " + frame.size());
        frame.pop(2);
        System.out.println("Stack size after popping 2 elements: " + frame.size());
    }
}
public class StackFrame {
    private int[] stack;
    private int top;

    public StackFrame(int size) {
        stack = new int[size];
        top = -1;
    }

    public void push(int value) {
        if (top < stack.length - 1) {
            stack[++top] = value;
        } else {
            throw new StackOverflowError("Stack is full");
        }
    }

    /**
     * Estrae un tipo astratto dallo stack del frame di output e restituisce il suo valore.
     * @return il tipo astratto che è stato estratto dallo stack del frame di output.
     */
    private int pop() {
        if (top >= 0) {
            return stack[top--];
        } else {
            throw new IllegalStateException("Stack is empty");
        }
    }

    public static void main(String[] args) {
        StackFrame frame = new StackFrame(5);
        frame.push(10);
        frame.push(20);
        System.out.println("Popped value: " + frame.pop()); // Should print 20
        System.out.println("Popped value: " + frame.pop()); // Should print 10
    }
}
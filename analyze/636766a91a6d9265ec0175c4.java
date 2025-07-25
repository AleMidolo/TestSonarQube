import java.util.Stack;

public class StackManipulator {
    private Stack<String> stack;

    public StackManipulator() {
        this.stack = new Stack<>();
    }

    /**
     * Rimuove quanti più tipi astratti possibile dallo stack del frame di output come descritto dal descrittore fornito.
     * @param descriptor un tipo o un descrittore di metodo (nel qual caso vengono rimossi i suoi tipi di argomento).
     */
    private void pop(final String descriptor) {
        // Assuming descriptor is a method descriptor like "(I)V" for int parameter
        if (descriptor.startsWith("(") && descriptor.contains(")")) {
            int start = descriptor.indexOf('(') + 1;
            int end = descriptor.indexOf(')');
            String parameters = descriptor.substring(start, end);
            for (String type : parameters.split(",")) {
                if (!stack.isEmpty() && stack.peek().equals(type)) {
                    stack.pop();
                }
            }
        } else {
            // If it's a single type, just pop it if it matches
            if (!stack.isEmpty() && stack.peek().equals(descriptor)) {
                stack.pop();
            }
        }
    }

    public void push(String type) {
        stack.push(type);
    }

    public Stack<String> getStack() {
        return stack;
    }

    public static void main(String[] args) {
        StackManipulator sm = new StackManipulator();
        sm.push("I");
        sm.push("J");
        sm.push("I");
        sm.push("F");

        System.out.println("Stack before pop: " + sm.getStack());
        sm.pop("(I)V");
        System.out.println("Stack after pop: " + sm.getStack());
    }
}
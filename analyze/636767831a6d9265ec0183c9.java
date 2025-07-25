public class DiagnosticContext {
    private static final ThreadLocal<Stack<String>> contextStack = ThreadLocal.withInitial(Stack::new);

    /** 
     * Osserva l'ultimo contesto diagnostico in cima a questo NDC senza rimuoverlo. <p>Il valore restituito è il valore che è stato inserito per ultimo. Se non è disponibile alcun contesto, viene restituita la stringa vuota "".
     * @return String Il contesto diagnostico più interno.
     */
    public static String peek() {
        Stack<String> stack = contextStack.get();
        return stack.isEmpty() ? "" : stack.peek();
    }

    public static void push(String context) {
        contextStack.get().push(context);
    }

    public static void pop() {
        Stack<String> stack = contextStack.get();
        if (!stack.isEmpty()) {
            stack.pop();
        }
    }

    public static void main(String[] args) {
        push("Context1");
        push("Context2");
        System.out.println(peek()); // Should print "Context2"
        pop();
        System.out.println(peek()); // Should print "Context1"
        pop();
        System.out.println(peek()); // Should print ""
    }
}
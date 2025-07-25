public class StringBuilderExample {
    private StringBuilder builder;

    public StringBuilderExample() {
        this.builder = new StringBuilder();
    }

    /** 
     * <p> Ottiene la String costruita da questo builder. </p>
     * @return la stringa costruita
     */
    public String toString() {
        return builder.toString();
    }

    public void append(String str) {
        builder.append(str);
    }

    public static void main(String[] args) {
        StringBuilderExample example = new StringBuilderExample();
        example.append("Hello, ");
        example.append("World!");
        System.out.println(example.toString()); // Output: Hello, World!
    }
}
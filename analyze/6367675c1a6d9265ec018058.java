import java.util.function.Supplier;

@SuppressWarnings("unchecked") 
public static Supplier<String> createStringSupplier(int start) {
    return new Supplier<String>() {
        private int current = start;

        @Override
        public String get() {
            return String.valueOf(current++);
        }
    };
}
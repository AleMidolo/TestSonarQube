private int computeBinaryLog(int n) {
    if (n <= 0) {
        throw new IllegalArgumentException("Input must be a positive integer.");
    }
    return (int) (Math.log(n) / Math.log(2)) + 1;
}
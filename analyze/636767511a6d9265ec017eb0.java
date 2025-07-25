public class NonZeroCounter {
    
    /** 
     * Ottiene il numero di voci diverse da zero in una riga.
     * @param row la riga
     * @return il numero di voci diverse da zero in una riga
     */
    public int nonZeros(int[] row) {
        int count = 0;
        for (int value : row) {
            if (value != 0) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        NonZeroCounter counter = new NonZeroCounter();
        int[] row = {1, 0, 2, 3, 0, 4};
        System.out.println("Numero di voci diverse da zero: " + counter.nonZeros(row));
    }
}
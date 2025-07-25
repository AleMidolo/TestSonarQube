public class LineNumberManager {
    
    private List<Integer> lineNumbers;

    public LineNumberManager() {
        lineNumbers = new ArrayList<>();
    }

    /** 
     * Aggiunge un numero di riga sorgente corrispondente a questa etichetta.
     * @param lineNumber un numero di riga sorgente (che dovrebbe essere strettamente positivo).
     */
    final void addLineNumber(final int lineNumber) {
        if (lineNumber <= 0) {
            throw new IllegalArgumentException("Il numero di riga deve essere strettamente positivo.");
        }
        lineNumbers.add(lineNumber);
    }

    public List<Integer> getLineNumbers() {
        return new ArrayList<>(lineNumbers);
    }

    public static void main(String[] args) {
        LineNumberManager manager = new LineNumberManager();
        manager.addLineNumber(5);
        manager.addLineNumber(10);
        System.out.println(manager.getLineNumbers());
    }
}
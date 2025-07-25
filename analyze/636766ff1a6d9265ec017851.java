public class ByteFinder {
    
    private byte[] buffer;

    public ByteFinder(byte[] buffer) {
        this.buffer = buffer;
    }

    /** 
     * Cerca un byte di valore specificato nel <code>buffer</code>, partendo dalla <code>posizione</code> specificata.
     * @param value Il valore da cercare.
     * @param pos   La posizione di partenza per la ricerca.
     * @return La posizione del byte trovato, contando dall'inizio del <code>buffer</code>, oppure <code>-1</code> se non trovato.
     */
    protected int findByte(byte value, int pos) {
        if (pos < 0 || pos >= buffer.length) {
            return -1; // posizione non valida
        }
        
        for (int i = pos; i < buffer.length; i++) {
            if (buffer[i] == value) {
                return i; // byte trovato
            }
        }
        
        return -1; // byte non trovato
    }

    public static void main(String[] args) {
        byte[] data = {1, 2, 3, 4, 5, 2};
        ByteFinder finder = new ByteFinder(data);
        int position = finder.findByte((byte) 2, 0);
        System.out.println("Byte trovato alla posizione: " + position);
    }
}
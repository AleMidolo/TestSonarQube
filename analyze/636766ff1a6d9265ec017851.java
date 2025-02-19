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
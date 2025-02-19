int visitFrameStart(final int offset, final int numLocal, final int numStack) {
    // Logica per iniziare la visita di un nuovo frame della mappa dello stack
    // Memorizza l'offset, il numero di variabili locali e il numero di elementi nello stack
    this.currentFrame = new Frame(offset, numLocal, numStack);
    
    // Restituisce l'indice del prossimo elemento da scrivere in questo frame
    return this.currentFrame.getNextIndex();
}
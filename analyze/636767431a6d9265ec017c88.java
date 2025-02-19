private List<Integer> computeLowerBounds(List<K> keys) {
    List<Integer> lowerBounds = new ArrayList<>();
    for (K key : keys) {
        // Logica per calcolare il limite inferiore per la chiave
        int lowerBound = calculateLowerBoundForKey(key);
        lowerBounds.add(lowerBound);
    }
    return lowerBounds;
}

private int calculateLowerBoundForKey(K key) {
    // Implementazione della logica per calcolare il limite inferiore per una chiave specifica
    // Questo è un esempio e dovrebbe essere sostituito con la logica reale
    return key.hashCode() % 100; // Esempio di calcolo
}
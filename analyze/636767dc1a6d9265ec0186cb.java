public void init() {
    // Controlla il percorso di distribuzione
    String distributionPath = System.getProperty("distribution.path");
    if (distributionPath == null || distributionPath.isEmpty()) {
        throw new IllegalArgumentException("Il percorso di distribuzione non è stato configurato.");
    }
    
    // Ulteriori inizializzazioni possono essere aggiunte qui
    System.out.println("Configurazione inizializzata con successo. Percorso di distribuzione: " + distributionPath);
}
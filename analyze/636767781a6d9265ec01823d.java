protected void subAppend(LoggingEvent event) {
    // Implementazione della scrittura effettiva del LoggingEvent
    if (event != null) {
        // Esegui la scrittura del LoggingEvent
        System.out.println("Logging event: " + event.getMessage());
        // Aggiungere ulteriori logiche di scrittura se necessario
    }
}
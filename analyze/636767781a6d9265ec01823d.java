import org.apache.log4j.spi.LoggingEvent;

public class CustomAppender {

    /**
     * Questo metodo esegue la scrittura effettiva
     */
    protected void subAppend(LoggingEvent event) {
        // Implementazione della scrittura del LoggingEvent
        if (event != null) {
            String message = event.getRenderedMessage();
            System.out.println("Logging Event: " + message);
            // Qui si può aggiungere ulteriore logica per gestire l'evento di logging
        }
    }
}
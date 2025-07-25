import org.apache.log4j.spi.LoggingEvent;

public class LoggerFormatter {

    /**
     * Formatta un evento di logging per un writer.
     * @param event evento di logging da formattare.
     * @return una stringa formattata dell'evento di logging.
     */
    public String format(final LoggingEvent event) {
        StringBuilder formattedEvent = new StringBuilder();
        formattedEvent.append("Timestamp: ").append(event.getTimeStamp()).append("\n");
        formattedEvent.append("Level: ").append(event.getLevel()).append("\n");
        formattedEvent.append("Logger: ").append(event.getLoggerName()).append("\n");
        formattedEvent.append("Message: ").append(event.getRenderedMessage()).append("\n");
        formattedEvent.append("Thread: ").append(event.getThreadName()).append("\n");
        
        if (event.getThrowableInformation() != null) {
            formattedEvent.append("Exception: ").append(event.getThrowableInformation().getThrowable().toString()).append("\n");
        }
        
        return formattedEvent.toString();
    }
}
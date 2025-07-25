import org.apache.log4j.spi.LoggingEvent;
import java.text.SimpleDateFormat;
import java.util.Date;

public class LoggerFormatter {

    /** 
     * Produce una stringa formattata come specificato dal modello di conversione.
     */
    public String format(LoggingEvent event) {
        StringBuilder formattedString = new StringBuilder();
        
        // Example formatting
        formattedString.append("Timestamp: ")
                       .append(new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date(event.getTimeStamp())))
                       .append(" | Level: ")
                       .append(event.getLevel())
                       .append(" | Message: ")
                       .append(event.getRenderedMessage());
        
        return formattedString.toString();
    }
}
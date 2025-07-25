import org.apache.log4j.spi.LoggingEvent;
import org.apache.log4j.Filter;

public class FilterDecider {

    /**
     * Restituisce {@link Filter#NEUTRAL} se non c'è corrispondenza con la stringa.
     */
    public int decide(LoggingEvent event) {
        // Assuming we are checking for a specific string match in the LoggingEvent
        String message = event.getMessage();
        String targetString = "specificString"; // Replace with the actual string to match

        if (!message.contains(targetString)) {
            return Filter.NEUTRAL;
        }
        
        // Additional logic can be added here for other cases
        return Filter.DENY; // Example return value if there's a match
    }
}
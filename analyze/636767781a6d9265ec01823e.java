import org.apache.log4j.AppenderSkeleton;
import org.apache.log4j.spi.LoggingEvent;

public class CustomAppender extends AppenderSkeleton {

    @Override
    protected void append(LoggingEvent event) {
        // Get the message from the logging event
        String message = event.getRenderedMessage();
        
        // Here you would implement the logic to send the message to each connected client
        // For demonstration purposes, we'll just print it to the console
        System.out.println("Logging to clients: " + message);
        
        // You can add your logic to handle connected clients and send the message to them
    }

    @Override
    public void close() {
        // Implement any cleanup logic if necessary
    }

    @Override
    public boolean requiresLayout() {
        return false; // Change to true if you are using a layout
    }
}
import javax.swing.SwingUtilities;
import java.util.logging.LogRecord;

public class Logger {
    
    public void addMessage(final LogRecord lr) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                // Here you would add the log record to your LogTable
                // For example, assuming you have a method to update the LogTable:
                updateLogTable(lr);
            }
        });
    }

    private void updateLogTable(LogRecord lr) {
        // Implementation to update the LogTable with the log record
        // This is a placeholder for the actual log table update logic
        System.out.println("Log Message: " + lr.getMessage());
    }
}
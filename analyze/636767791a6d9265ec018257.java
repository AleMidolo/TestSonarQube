import javax.swing.SwingUtilities;
import java.util.logging.LogRecord;

public void addMessage(final LogRecord lr) {
    SwingUtilities.invokeLater(new Runnable() {
        @Override
        public void run() {
            // Assuming LogTable is a component that displays log messages
            LogTable.addLogRecord(lr);
        }
    });
}
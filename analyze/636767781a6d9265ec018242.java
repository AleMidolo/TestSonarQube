import java.util.List;

public class Logger {
    private List<Appender> appenders;

    public Logger(List<Appender> appenders) {
        this.appenders = appenders;
    }

    /** 
     * Chiama il metodo <code>doAppend</code> su tutti gli appender collegati.  
     */
    public int appendLoopOnAppenders(LoggingEvent event) {
        int appendCount = 0;
        for (Appender appender : appenders) {
            appender.doAppend(event);
            appendCount++;
        }
        return appendCount;
    }
}

interface Appender {
    void doAppend(LoggingEvent event);
}

class LoggingEvent {
    // Event details
}
public String format(final LoggingEvent event) {
    StringBuilder formattedEvent = new StringBuilder();
    formattedEvent.append("Timestamp: ").append(event.getTimestamp()).append("\n");
    formattedEvent.append("Level: ").append(event.getLevel()).append("\n");
    formattedEvent.append("Message: ").append(event.getMessage()).append("\n");
    formattedEvent.append("Logger: ").append(event.getLoggerName()).append("\n");
    formattedEvent.append("Thread: ").append(event.getThreadName()).append("\n");
    
    return formattedEvent.toString();
}
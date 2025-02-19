public String format(LoggingEvent event) {
    StringBuilder formattedString = new StringBuilder();
    
    // Example formatting logic
    formattedString.append("Timestamp: ").append(event.getTimestamp()).append("\n");
    formattedString.append("Level: ").append(event.getLevel()).append("\n");
    formattedString.append("Message: ").append(event.getMessage()).append("\n");
    formattedString.append("Thread: ").append(event.getThreadName()).append("\n");
    
    return formattedString.toString();
}
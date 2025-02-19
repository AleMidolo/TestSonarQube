public void add(LoggingEvent event) {
    if (event == null) {
        throw new IllegalArgumentException("Event cannot be null");
    }
    // Assuming there's a list to hold the events
    eventBuffer.add(event);
}
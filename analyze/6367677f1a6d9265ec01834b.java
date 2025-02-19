public void put(LoggingEvent o) {
    if (buffer.size() < bufferCapacity) {
        buffer.add(o);
    }
}
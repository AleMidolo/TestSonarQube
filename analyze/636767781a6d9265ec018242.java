public int appendLoopOnAppenders(LoggingEvent event) {
    int appendCount = 0;
    for (Appender appender : getAppenders()) {
        if (appender != null) {
            appender.doAppend(event);
            appendCount++;
        }
    }
    return appendCount;
}
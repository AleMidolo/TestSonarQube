public void addNewTarget(Channels channels, IConsumer consumer) {
    if (channels == null || consumer == null) {
        throw new IllegalArgumentException("Channels and consumer cannot be null");
    }
    channels.addConsumer(consumer);
}
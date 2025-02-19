public boolean isExpired(long timestamp, long expiredThreshold) {
    long currentTime = System.currentTimeMillis();
    return (currentTime - timestamp) > expiredThreshold;
}
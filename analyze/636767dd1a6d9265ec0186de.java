public class CacheExpiration {

    /** 
     * @param timestamp        tempo attuale
     * @param expiredThreshold rappresenta la durata tra l'ultimo aggiornamento e il momento in cui si rimuove dalla cache.
     * @return true significa che queste metriche devono essere rimosse dalla cache.
     */
    public boolean isExpired(long timestamp, long expiredThreshold) {
        long currentTime = System.currentTimeMillis();
        return (currentTime - timestamp) > expiredThreshold;
    }

    public static void main(String[] args) {
        CacheExpiration cacheExpiration = new CacheExpiration();
        long timestamp = System.currentTimeMillis() - 5000; // 5 seconds ago
        long expiredThreshold = 3000; // 3 seconds

        boolean result = cacheExpiration.isExpired(timestamp, expiredThreshold);
        System.out.println("Is expired: " + result); // Should print true
    }
}
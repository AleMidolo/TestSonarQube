public class TimestampManager {
    private long lastWriteTimeStamp;

    /** 
     * L'ultima volta, in millisecondi, in cui è avvenuta un'operazione di scrittura.
     * @return questo
     */
    public long lastWriteTimeStampInMilliseconds() {
        return lastWriteTimeStamp;
    }

    public void updateLastWriteTimeStamp() {
        lastWriteTimeStamp = System.currentTimeMillis();
    }

    public static void main(String[] args) {
        TimestampManager manager = new TimestampManager();
        manager.updateLastWriteTimeStamp();
        System.out.println("Last write timestamp in milliseconds: " + manager.lastWriteTimeStampInMilliseconds());
    }
}
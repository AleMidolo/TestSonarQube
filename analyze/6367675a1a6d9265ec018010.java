public class Bucket {
    // Assuming there is a data structure to hold the buckets
    private static List<Bucket> bucketList = new ArrayList<>();

    /** 
     * Rimuove questo bucket dalla struttura dati.
     */
    public void removeSelf() {
        bucketList.remove(this);
    }
}
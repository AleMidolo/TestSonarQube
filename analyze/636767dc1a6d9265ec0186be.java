public class TimeBucketCompressor {

    /**
     * Segui il valore di dayStep per riformattare il valore numerico "long" del bucket temporale. 
     * Ad esempio, se dayStep == 11, il bucket di tempo riformattato per 20000105 è 20000101, 
     * per 20000115 è 20000112, e per 20000123 è 20000123.
     */
    static long compressTimeBucket(long timeBucket, int dayStep) {
        // Convert the long timeBucket to a string to manipulate the date
        String timeBucketStr = String.valueOf(timeBucket);
        
        // Extract year, month, and day from the timeBucket
        int year = Integer.parseInt(timeBucketStr.substring(0, 4));
        int month = Integer.parseInt(timeBucketStr.substring(4, 6));
        int day = Integer.parseInt(timeBucketStr.substring(6, 8));
        
        // Calculate the base day for the compression
        int baseDay = (day - 1) / dayStep * dayStep + 1;
        
        // Handle month overflow
        if (baseDay > 28) {
            if (baseDay > 31) {
                baseDay = 1;
                month++;
                if (month > 12) {
                    month = 1;
                    year++;
                }
            }
            // Adjust for months with less than 31 days
            if (month == 2 && baseDay > 28) {
                baseDay = 28; // Simplified for leap years
            } else if ((month == 4 || month == 6 || month == 9 || month == 11) && baseDay > 30) {
                baseDay = 30;
            }
        }
        
        // Format the new date back to long
        String newTimeBucketStr = String.format("%04d%02d%02d", year, month, baseDay);
        return Long.parseLong(newTimeBucketStr);
    }

    public static void main(String[] args) {
        // Example usage
        long compressedBucket = compressTimeBucket(20000115L, 11);
        System.out.println(compressedBucket); // Output: 20000112
    }
}
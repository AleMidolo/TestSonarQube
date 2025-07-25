import java.util.Arrays;

public class ArrayComparer {
    
    /** 
     * Restituisce true se i contenuti dell'array interno e dell'array fornito corrispondono.
     */
    public boolean equals(final byte[] data, int offset, final int len) {
        if (data == null || offset < 0 || len < 0 || offset + len > data.length) {
            return false;
        }
        
        byte[] internalArray = getInternalArray(); // Assume this method retrieves the internal array
        if (internalArray.length < len) {
            return false;
        }
        
        for (int i = 0; i < len; i++) {
            if (internalArray[i] != data[offset + i]) {
                return false;
            }
        }
        
        return true;
    }
    
    private byte[] getInternalArray() {
        // This method should return the internal byte array for comparison
        return new byte[] {1, 2, 3, 4, 5}; // Example internal array
    }
}
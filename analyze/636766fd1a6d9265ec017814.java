public class ArrayComparator {
    
    /** 
     * Confronta i <code>count</code> primi byte negli array <code>a</code> e <code>b</code>.
     * @param a     Il primo array da confrontare.
     * @param b     Il secondo array da confrontare.
     * @param count Quanti byte devono essere confrontati.
     * @return <code>true</code> se i <code>count</code> primi byte negli array <code>a</code> e <code>b</code> sono uguali.
     */
    public static boolean arrayequals(byte[] a, byte[] b, int count) {
        if (a == null || b == null || count < 0 || count > a.length || count > b.length) {
            return false;
        }
        for (int i = 0; i < count; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        byte[] array1 = {1, 2, 3, 4, 5};
        byte[] array2 = {1, 2, 3, 6, 7};
        int count = 3;

        boolean result = arrayequals(array1, array2, count);
        System.out.println("I primi " + count + " byte sono uguali: " + result);
    }
}
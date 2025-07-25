import java.util.ArrayList;
import java.util.List;

public class ArrayConcatenation {

    /** 
     * Concatenare i dati degli array di Stringa forniti in uno solo, includendo gli elementi sovrapposti due volte. 
     * <p>L'ordine degli elementi negli array originali è preservato.
     * @param array1 il primo array (può essere <code>null</code>)
     * @param array2 il secondo array (può essere <code>null</code>)
     * @return il nuovo array (<code>null</code> se entrambi gli array forniti erano <code>null</code>)
     */
    public static String[] concatenateStringArrays(String[] array1, String[] array2) {
        if (array1 == null && array2 == null) {
            return null;
        }

        List<String> resultList = new ArrayList<>();

        if (array1 != null) {
            for (String s : array1) {
                resultList.add(s);
            }
        }

        if (array2 != null) {
            for (String s : array2) {
                resultList.add(s);
            }
        }

        // Include overlapping elements twice
        if (array1 != null && array2 != null) {
            for (String s : array1) {
                for (String t : array2) {
                    if (s.equals(t)) {
                        resultList.add(s);
                    }
                }
            }
        }

        return resultList.toArray(new String[0]);
    }

    public static void main(String[] args) {
        String[] array1 = {"a", "b", "c"};
        String[] array2 = {"b", "c", "d"};
        String[] result = concatenateStringArrays(array1, array2);
        
        for (String s : result) {
            System.out.print(s + " ");
        }
    }
}
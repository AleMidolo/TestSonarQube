import java.util.Arrays;

public class StringArrayUtil {
    /** 
     * Aggiunge la Stringa fornita all'array di Stringhe dato, restituendo un nuovo array che consiste nei contenuti dell'array di input più la Stringa fornita.
     * @param array l'array a cui aggiungere (può essere <code>null</code>)
     * @param str la Stringa da aggiungere
     * @return il nuovo array (mai <code>null</code>)
     */
    public static String[] addStringToArray(String[] array, String str) {
        if (array == null) {
            return new String[]{str};
        }
        String[] newArray = Arrays.copyOf(array, array.length + 1);
        newArray[array.length] = str;
        return newArray;
    }
}
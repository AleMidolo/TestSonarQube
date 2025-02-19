import java.util.Enumeration;
import java.util.Vector;

public static String[] toStringArray(Enumeration<String> enumeration) {
    if (enumeration == null) {
        return null;
    }
    
    Vector<String> vector = new Vector<>();
    while (enumeration.hasMoreElements()) {
        vector.add(enumeration.nextElement());
    }
    
    return vector.toArray(new String[0]);
}
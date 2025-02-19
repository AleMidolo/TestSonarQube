import java.util.Collection;
import java.util.Iterator;

static String[] toNoNullStringArray(Collection<?> collection) {
    if (collection == null) {
        return new String[0];
    }
    
    // Create an array of the same size as the collection
    String[] result = new String[collection.size()];
    Iterator<?> iterator = collection.iterator();
    int index = 0;

    while (iterator.hasNext()) {
        Object element = iterator.next();
        if (element != null) {
            result[index++] = element.toString();
        }
    }

    // Resize the array to remove nulls
    String[] noNullResult = new String[index];
    System.arraycopy(result, 0, noNullResult, 0, index);
    
    return noNullResult;
}
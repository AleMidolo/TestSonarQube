import java.util.List;

public static boolean containsAnyIgnoreCase(String str, List<String> searchStrArray) {
    if (str == null || searchStrArray == null) {
        return false;
    }
    String lowerStr = str.toLowerCase();
    for (String searchStr : searchStrArray) {
        if (searchStr != null && lowerStr.contains(searchStr.toLowerCase())) {
            return true;
        }
    }
    return false;
}
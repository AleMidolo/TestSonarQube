public static int countOccurrencesOf(String str, String sub) {
    if (str == null || sub == null) {
        return 0;
    }
    
    int count = 0;
    int index = 0;
    
    while ((index = str.indexOf(sub, index)) != -1) {
        count++;
        index += sub.length();
    }
    
    return count;
}
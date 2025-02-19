public static String[] concatenateStringArrays(String[] array1, String[] array2) {
    if (array1 == null && array2 == null) {
        return null;
    }

    int length1 = (array1 != null) ? array1.length : 0;
    int length2 = (array2 != null) ? array2.length : 0;
    String[] result = new String[length1 + length2];

    int index = 0;
    if (array1 != null) {
        for (String s : array1) {
            result[index++] = s;
        }
    }
    if (array2 != null) {
        for (String s : array2) {
            result[index++] = s;
        }
    }

    return result;
}
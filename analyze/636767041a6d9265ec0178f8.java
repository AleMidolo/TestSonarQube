private static String[] copiaStringhe(final String[] src) {
    if (src == null) {
        return null;
    }
    
    String[] dst = new String[src.length];
    for (int i = 0; i < src.length; i++) {
        dst[i] = src[i] != null ? src[i].toLowerCase() : null;
    }
    
    return dst;
}
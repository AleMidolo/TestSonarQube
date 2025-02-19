import java.util.Base64;

public static String base64Decode(final String s) {
    if (s == null || s.isEmpty()) {
        return "";
    }
    byte[] decodedBytes = Base64.getDecoder().decode(s);
    return new String(decodedBytes);
}
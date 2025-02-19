import java.nio.charset.StandardCharsets;

public static LinkedBuffer writeUTF8(final CharSequence str, final WriteSession session, final LinkedBuffer lb) {
    if (str == null || lb == null) {
        throw new IllegalArgumentException("Input string and LinkedBuffer cannot be null");
    }
    
    byte[] bytes = str.toString().getBytes(StandardCharsets.UTF_8);
    lb.write(bytes);
    
    return lb;
}
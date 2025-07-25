import java.nio.charset.Charset;

public class CharsetTranslator {

    /** 
     * Traduci un nome di set di caratteri standard MIME nell'equivalente Java.
     * @param charset Il nome standard MIME.
     * @return L'equivalente Java per questo nome.
     */
    private static String javaCharset(String charset) {
        Charset javaCharset = Charset.forName(charset);
        return javaCharset.name();
    }

    public static void main(String[] args) {
        // Esempio di utilizzo
        String mimeCharset = "UTF-8";
        String javaEquivalent = javaCharset(mimeCharset);
        System.out.println("L'equivalente Java per " + mimeCharset + " è: " + javaEquivalent);
    }
}
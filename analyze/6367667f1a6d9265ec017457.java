import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

public class OctetDecoder {

    /** 
     * Decodifica gli ottetti in caratteri utilizzando la decodifica UTF-8 e aggiunge i caratteri ad uno oggetto StringBuffer.
     * @return l'indice del prossimo carattere non controllato nella stringa da decodificare
     */
    private static int decodeOctets(int i, ByteBuffer bb, StringBuilder sb) {
        while (i < bb.remaining()) {
            byte b = bb.get(i);
            if ((b & 0x80) == 0) { // 1-byte character
                sb.append((char) b);
                i++;
            } else if ((b & 0xE0) == 0xC0) { // 2-byte character
                if (i + 1 < bb.remaining()) {
                    sb.append(new String(new byte[]{b, bb.get(i + 1)}, StandardCharsets.UTF_8));
                    i += 2;
                } else {
                    break; // incomplete character
                }
            } else if ((b & 0xF0) == 0xE0) { // 3-byte character
                if (i + 2 < bb.remaining()) {
                    sb.append(new String(new byte[]{b, bb.get(i + 1), bb.get(i + 2)}, StandardCharsets.UTF_8));
                    i += 3;
                } else {
                    break; // incomplete character
                }
            } else if ((b & 0xF8) == 0xF0) { // 4-byte character
                if (i + 3 < bb.remaining()) {
                    sb.append(new String(new byte[]{b, bb.get(i + 1), bb.get(i + 2), bb.get(i + 3)}, StandardCharsets.UTF_8));
                    i += 4;
                } else {
                    break; // incomplete character
                }
            } else {
                // Invalid UTF-8 byte, skip it
                i++;
            }
        }
        return i;
    }
}
import java.io.IOException;
import java.io.InputStream;

public class TagReader {
    private InputStream inputStream;

    public TagReader(InputStream inputStream) {
        this.inputStream = inputStream;
    }

    /** 
     * Tentativo di leggere un tag di campo, restituendo zero se abbiamo raggiunto la fine del file (EOF). 
     * I parser di messaggi di protocollo utilizzano questo metodo per leggere i tag, poiché un messaggio di protocollo 
     * può legalmente terminare ovunque si trovi un tag, e zero non è un numero di tag valido.
     */
    public int readTag() throws IOException {
        int tag = inputStream.read();
        if (tag == -1) {
            return 0; // EOF reached
        }
        return tag; // Return the read tag
    }
}
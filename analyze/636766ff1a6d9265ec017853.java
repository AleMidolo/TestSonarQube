import org.objectweb.asm.Label;

public class LabelManager {

    /**
     * Restituisce l'etichetta corrispondente all'offset di bytecode fornito. L'implementazione predefinita di questo metodo crea un'etichetta per l'offset dato se non è già stata creata.
     * @param bytecodeOffset un offset di bytecode in un metodo.
     * @param labels le etichette già create, indicizzate per il loro offset. Se un'etichetta esiste già per bytecodeOffset, questo metodo non deve crearne una nuova. Altrimenti, deve memorizzare la nuova etichetta in questo array.
     * @return un'etichetta non nulla, che deve essere uguale a labels[bytecodeOffset].
     */
    protected Label readLabel(final int bytecodeOffset, final Label[] labels) {
        if (labels[bytecodeOffset] == null) {
            labels[bytecodeOffset] = new Label();
        }
        return labels[bytecodeOffset];
    }
}
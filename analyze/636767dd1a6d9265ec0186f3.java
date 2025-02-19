/**
 * Mantieni lo stesso nome da sostituire come {@link ColumnName#overrideName(String,String)}
 * @param oldName da sostituire.
 * @param newName da utilizzare a livello di archiviazione.
 */
public void overrideName(String oldName, String newName) {
    // Implementazione della logica per sostituire il nome
    // Questo è un esempio di come potrebbe essere implementato
    if (oldName == null || newName == null) {
        throw new IllegalArgumentException("I nomi non possono essere null");
    }
    
    // Logica per sostituire oldName con newName
    // Potrebbe includere la modifica di una mappa o di un database
    System.out.println("Sostituito " + oldName + " con " + newName);
}
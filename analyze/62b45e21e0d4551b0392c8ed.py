def find_path_type(path):
    """
    Restituisce una stringa che indica il tipo di elemento presente nel percorso specificato.

    Valori restituiti:
        'root' - sembra essere una Radice di Archiviazione OCFL (OCFL Storage Root)
        'object' - sembra essere un Oggetto OCFL (OCFL Object)
        'file' - un file, potrebbe essere un inventario
        altra stringa - descrive un errore o una spiegazione del problema

    Si basa esclusivamente sui file "0=*" Namaste per determinare il tipo di directory.
    """
    import os

    if not os.path.exists(path):
        return "Il percorso specificato non esiste."

    if os.path.isdir(path):
        if any(file.startswith("0=") for file in os.listdir(path)):
            if "inventory" in os.listdir(path):
                return "object"
            return "root"
        return "altra stringa: nessun file '0=*' trovato."

    if os.path.isfile(path):
        return "file"

    return "altra stringa: tipo di elemento sconosciuto."
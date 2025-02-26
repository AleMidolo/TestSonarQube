import os

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
    if not os.path.exists(path):
        return "Il percorso specificato non esiste."

    if os.path.isdir(path):
        # Controlla se ci sono file che iniziano con "0="
        for item in os.listdir(path):
            if item.startswith("0="):
                if "inventory" in item:
                    return "file"
                return "object"
        return "root"
    
    if os.path.isfile(path):
        return "file"
    
    return "Tipo di elemento sconosciuto."
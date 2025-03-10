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
    
    if os.path.isfile(path):
        return "file"
    
    namaste_files = [f for f in os.listdir(path) if f.startswith("0=")]
    
    if not namaste_files:
        return "La directory non contiene file Namaste."
    
    if len(namaste_files) > 1:
        return "La directory contiene più file Namaste, il che non è previsto."
    
    namaste_file = namaste_files[0]
    with open(os.path.join(path, namaste_file), 'r') as f:
        content = f.read().strip()
    
    if content == "ocfl_1.0":
        return "root"
    elif content == "ocfl_object_1.0":
        return "object"
    else:
        return f"Contenuto del file Namaste non riconosciuto: {content}"
def match_file_by_prefix(prefix, file_path):
    """
    Identifica se un `file_path` appartiene a un pacchetto di documenti in base a un determinato `prefix`.

    Restituisce `True` per i documenti che appartengono a un pacchetto.

    Parametri
    ----------
    prefix : str  
        Prefisso del nome del file  

    file_path : str  
        Percorso del file  
    Restituisce
    -------
    bool  
        `True` - il file appartiene al pacchetto
    """
    # Extract filename from path
    filename = file_path.split('/')[-1]
    
    # Check if filename starts with prefix
    return filename.startswith(prefix)
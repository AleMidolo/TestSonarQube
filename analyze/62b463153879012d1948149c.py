def select_filenames_by_prefix(prefix, files):
    """
    Ottieni i file che appartengono a un pacchetto di documenti.

    Restituisce i file della lista `files` i cui nomi iniziano con il prefisso `prefix`.

    Parametri
    ----------
    prefix : `str`  
        Prefisso del nome del file.  

    files : `list` di `str`  
        Percorsi dei file.  

    Ritorno
    -------
    list  
        Percorsi dei file i cui nomi base corrispondono al prefisso specificato.  
    """
    return [file for file in files if file.startswith(prefix)]
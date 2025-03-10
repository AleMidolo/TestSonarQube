import os

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
    selected_files = []
    for file_path in files:
        file_name = os.path.basename(file_path)
        if file_name.startswith(prefix):
            selected_files.append(file_path)
    return selected_files
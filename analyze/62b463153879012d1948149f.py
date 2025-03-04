def _eval_file(prefix, file_path):
    """
    Identifica il tipo di file del pacchetto: `asset` o `rendition`.

    Identifica il tipo di file del pacchetto e aggiorna `packages` con il tipo e
    il percorso del file in analisi.

    Parametri
    ----------
    prefix : str
        Nome del file XML senza estensione.
    filename : str
        Nome del file.
    file_folder : str
        Cartella del file.

    Restituisce
    -------
    dict
    """
    result = {}
    
    # Extract filename from path
    filename = file_path.split('/')[-1]
    
    # Check if file is an asset or rendition
    if filename.startswith(prefix):
        if '_rendition' in filename:
            result['type'] = 'rendition'
        else:
            result['type'] = 'asset'
        result['path'] = file_path
        
    return result
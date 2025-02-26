def _eval_file(prefix, file_path):
    """
    Identifica il tipo di file del pacchetto: `asset` o `rendition`.

    Identifica il tipo di file del pacchetto e aggiorna `packages` con il tipo e
    il percorso del file in analisi.

    Parametri
    ----------
    prefix : str
        Nome del file XML senza estensione.
    file_path : str
        Nome del file.

    Restituisce
    -------
    dict
    """
    import os

    # Initialize the result dictionary
    result = {}

    # Determine the file type based on the file extension
    _, file_extension = os.path.splitext(file_path)
    
    if file_extension in ['.jpg', '.png', '.gif']:
        file_type = 'asset'
    elif file_extension in ['.pdf', '.docx', '.pptx']:
        file_type = 'rendition'
    else:
        file_type = 'unknown'

    # Update the result dictionary
    result['type'] = file_type
    result['path'] = file_path

    return result
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
    import os

    # Initialize the result dictionary
    result = {}

    # Extract the file name and extension
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1].lower()

    # Determine the type of file based on its extension
    if file_extension in ['.xml', '.json']:
        file_type = 'asset'
    elif file_extension in ['.jpg', '.png', '.pdf']:
        file_type = 'rendition'
    else:
        file_type = 'unknown'

    # Update the result dictionary
    result['type'] = file_type
    result['path'] = file_path

    return result
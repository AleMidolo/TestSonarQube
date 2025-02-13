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

    packages = {}
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1].lower()

    if file_extension in ['.jpg', '.png', '.gif']:
        file_type = 'asset'
    elif file_extension in ['.pdf', '.docx', '.pptx']:
        file_type = 'rendition'
    else:
        file_type = 'unknown'

    packages[prefix] = {
        'type': file_type,
        'path': file_path
    }

    return packages
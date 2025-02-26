def _explore_zipfile(zip_path):
    """
    Ottiene i dati dei pacchetti dal percorso zip fornito.

    Raggruppa i file in base al nome base dei loro file XML e restituisce i dati in formato dizionario.

    Parametri
    ----------
    zip_path : str  
        Percorso del file zip.

    Restituisce
    -------
    dict
    """
    import zipfile
    from collections import defaultdict
    import os

    data_dict = defaultdict(list)

    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        for file_info in zip_file.infolist():
            if file_info.filename.endswith('.xml'):
                base_name = os.path.splitext(os.path.basename(file_info.filename))[0]
                with zip_file.open(file_info.filename) as file:
                    data_dict[base_name].append(file.read())

    return dict(data_dict)
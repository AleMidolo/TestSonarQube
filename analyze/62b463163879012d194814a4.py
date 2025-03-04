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
    import os
    from collections import defaultdict
    
    # Dizionario per raggruppare i file per nome base
    grouped_files = defaultdict(list)
    
    # Apre il file zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Itera su tutti i file nel zip
        for filename in zip_ref.namelist():
            # Ignora le directory
            if filename.endswith('/'):
                continue
                
            # Ottiene il nome base del file (senza estensione)
            base_name = os.path.splitext(os.path.basename(filename))[0]
            
            # Se il file è un XML
            if filename.endswith('.xml'):
                # Usa il nome base come chiave
                key = base_name
            else:
                # Per altri file, usa il nome base del file XML associato come chiave
                # Assumendo che il nome base sia tutto ciò che precede l'ultimo underscore
                key = base_name.rsplit('_', 1)[0]
            
            # Aggiunge il file al gruppo appropriato
            grouped_files[key].append({
                'filename': filename,
                'content': zip_ref.read(filename)
            })
    
    return dict(grouped_files)
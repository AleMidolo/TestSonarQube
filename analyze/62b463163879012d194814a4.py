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
        for file_name in zip_ref.namelist():
            # Ignora le directory
            if file_name.endswith('/'):
                continue
                
            # Ottiene il nome base del file (senza estensione)
            base_name = os.path.splitext(os.path.basename(file_name))[0]
            
            # Se il file è un XML
            if file_name.lower().endswith('.xml'):
                # Rimuove eventuali suffissi dopo il nome base
                base_name = base_name.split('_')[0]
                
            # Aggiunge il file al gruppo corrispondente
            grouped_files[base_name].append({
                'name': file_name,
                'data': zip_ref.read(file_name)
            })
    
    # Converte defaultdict in dict normale
    return dict(grouped_files)
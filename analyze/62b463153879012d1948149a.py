def _group_files_by_xml_filename(source, xmls, files):
    """
    Raggruppa i file per il nome base degli XML

    Raggruppa i file in base al nome base degli XML e restituisce i dati in formato dizionario.

    Parametri
    ----------
    xml_filename : str  
        Nomi dei file XML.  
    
    files: list  
        Lista dei file presenti nella cartella o nell'archivio zip.  
    
    Ritorna
    -------
    dict  
        - chiave: nome dei file XML.  
        - valore: Package.  
    """
    result = {}
    
    # Iterate through XML files
    for xml in xmls:
        # Get base filename without extension
        base_name = xml.rsplit('.', 1)[0]
        
        # Find all files that start with the XML base name
        matching_files = [f for f in files if f.startswith(base_name)]
        
        # Add to result dictionary
        if matching_files:
            result[xml] = {
                'source': source,
                'files': matching_files
            }
            
    return result
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
    grouped_files = {}
    
    for xml in xmls:
        base_name = xml.split('.')[0]  # Assuming the base name is the part before the first dot
        grouped_files[base_name] = []

        for file in files:
            if file.startswith(base_name):
                grouped_files[base_name].append(file)

    return grouped_files
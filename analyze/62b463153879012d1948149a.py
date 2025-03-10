def _group_files_by_xml_filename(source, xmls, files):
    """
    Raggruppa i file per il nome base degli XML.

    Raggruppa i file in base al nome base degli XML e restituisce i dati in formato dizionario.

    Parametri
    ----------
    source : str
        Percorso della cartella o dell'archivio zip.
    xmls : list
        Lista dei nomi dei file XML.
    files : list
        Lista dei file presenti nella cartella o nell'archivio zip.

    Ritorna
    -------
    dict
        - chiave: nome dei file XML.
        - valore: lista di file associati al nome XML.
    """
    grouped_files = {}
    
    for xml in xmls:
        xml_base = xml.split('.')[0]  # Estrae il nome base senza estensione
        grouped_files[xml] = [file for file in files if file.startswith(xml_base)]
    
    return grouped_files
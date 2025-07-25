def _group_files_by_xml_filename(source, xmls, files):
    """
    Agrupa archivos por el nombre base de su archivo XML.

    Agrupa los archivos según el nombre base de su archivo XML y devuelve los datos en formato dict.

    Parámetros
    ----------
    *xml_filename* : str  
        Nombres de los archivos XML.  

    *files* : list  
        Lista de archivos en la carpeta o archivo comprimido (zip).  

    Retorna
    -------
    *dict*
        *key*: Nombre de los archivos XML.  
        *name*: Paquete.  
    """
    result = {}
    
    # Iterate through XML files
    for xml in xmls:
        # Get base name without extension
        xml_base = xml.rsplit('.', 1)[0]
        
        # Find all files that start with the XML base name
        matching_files = [f for f in files if f.startswith(xml_base)]
        
        # Add to result dictionary
        if matching_files:
            result[xml] = {
                'name': xml_base,
                'files': matching_files,
                'source': source
            }
            
    return result
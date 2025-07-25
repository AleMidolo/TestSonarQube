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
    grouped_files = {}
    
    for xml in xmls:
        xml_base = xml.split('.')[0]  # Obtener el nombre base sin la extensión
        grouped_files[xml_base] = []
        
        for file in files:
            if file.startswith(xml_base):
                grouped_files[xml_base].append(file)
    
    return grouped_files
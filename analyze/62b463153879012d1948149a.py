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
        base_name = xml.rsplit('.', 1)[0]  # Get the base name without extension
        grouped_files[base_name] = []

        for file in files:
            if file.startswith(base_name):
                grouped_files[base_name].append(file)

    return grouped_files
def _group_files_by_xml_filename(source, xmls, files):
    """
    Agrupa archivos por el nombre base de su archivo XML.

    Agrupa los archivos según el nombre base de su archivo XML y devuelve los datos en formato dict.

    Parámetros
    ----------
    *source* : str
        Ruta de la carpeta o archivo comprimido (zip).
    
    *xmls* : list
        Nombres de los archivos XML.
    
    *files* : list
        Lista de archivos en la carpeta o archivo comprimido (zip).

    Retorna
    -------
    *dict*
        *key*: Nombre de los archivos XML.
        *value*: Lista de archivos asociados al XML.
    """
    grouped_files = {}
    
    for xml in xmls:
        xml_base = xml.split('.')[0]  # Obtener el nombre base sin la extensión
        grouped_files[xml] = [file for file in files if file.startswith(xml_base)]
    
    return grouped_files
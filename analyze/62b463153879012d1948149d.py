def _explore_folder(folder):
    """
    Obtiene los datos de los paquetes desde la carpeta.  

    Agrupa los archivos por el nombre base de su archivo XML y devuelve los datos en formato de diccionario.  

    Parámetros  
    ----------  
    folder : str  
        Carpeta del paquete  

    Retorna  
    -------  
    dict
    """
    import os
    from collections import defaultdict
    
    # Diccionario para almacenar los archivos agrupados
    files_dict = defaultdict(dict)
    
    # Recorrer todos los archivos en la carpeta
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        
        # Solo procesar archivos, no carpetas
        if os.path.isfile(filepath):
            # Obtener nombre base y extensión
            basename, ext = os.path.splitext(filename)
            
            # Si es XML, usar como clave base
            if ext.lower() == '.xml':
                files_dict[basename]['xml'] = filepath
            # Si es PDF, agregar a la entrada correspondiente
            elif ext.lower() == '.pdf':
                files_dict[basename]['pdf'] = filepath
                
    # Convertir defaultdict a dict normal
    return dict(files_dict)
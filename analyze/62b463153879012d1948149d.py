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
    
    # Diccionario para almacenar los archivos agrupados por nombre base
    files_by_base = defaultdict(dict)
    
    # Recorrer todos los archivos en la carpeta
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        
        # Solo procesar archivos, no directorios
        if os.path.isfile(filepath):
            # Obtener extensión y nombre base
            base, ext = os.path.splitext(filename)
            
            # Remover el guión y número al final del nombre base si existe
            # Ejemplo: "archivo-1.xml" -> "archivo"
            base = base.rsplit('-', 1)[0]
            
            # Guardar la ruta del archivo en el diccionario
            # usando la extensión como clave
            files_by_base[base][ext.lower()] = filepath
            
    return dict(files_by_base)
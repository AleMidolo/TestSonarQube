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
        
        # Ignorar directorios
        if os.path.isdir(filepath):
            continue
            
        # Obtener extensión y nombre base
        name, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        # Remover sufijos comunes para obtener el nombre base
        base_name = name
        if name.endswith(('.signed', '.xml')):
            base_name = name.rsplit('.', 1)[0]
            
        # Agrupar archivos por nombre base
        if ext == '.xml':
            files_by_base[base_name]['xml'] = filepath
        elif ext in ('.pdf', '.jpg', '.png'):
            files_by_base[base_name]['pdf'] = filepath
        elif ext == '.p7m':
            files_by_base[base_name]['p7m'] = filepath
            
    return dict(files_by_base)
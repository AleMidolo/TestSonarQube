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
    files_dict = defaultdict(list)
    
    # Recorrer todos los archivos en la carpeta
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        
        # Solo procesar archivos, no directorios
        if os.path.isfile(filepath):
            # Obtener el nombre base sin extensión
            base_name = os.path.splitext(filename)[0]
            
            # Si termina en números, obtener la parte base
            while base_name[-1].isdigit():
                base_name = base_name[:-1]
            
            # Agregar el archivo completo a la lista del nombre base
            files_dict[base_name].append({
                'filename': filename,
                'filepath': filepath
            })
            
    # Convertir defaultdict a dict normal
    return dict(files_dict)
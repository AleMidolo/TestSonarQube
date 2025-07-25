def select_filenames_by_prefix(prefix, files):
    """
    Obtén los archivos que pertenecen a un paquete de documentos.

    Retorna los archivos de la lista `files` cuyos nombres comienzan con `prefix`.

    Parámetros
    ----------
    prefix : str  
    Prefijo del nombre del archivo.  

    files : lista de str  
    Rutas de los archivos.  

    Retorna
    -------
    list  
    Lista de rutas de archivos cuyos nombres base coinciden con el prefijo `prefix`.
    """
    # Lista para almacenar los archivos que coinciden con el prefijo
    matching_files = []
    
    # Iterar sobre cada archivo en la lista
    for file in files:
        # Obtener el nombre base del archivo (sin la ruta)
        filename = file.split('/')[-1]
        
        # Verificar si el nombre del archivo comienza con el prefijo
        if filename.startswith(prefix):
            matching_files.append(file)
            
    return matching_files
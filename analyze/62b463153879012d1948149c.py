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
    return [file for file in files if file.startswith(prefix)]
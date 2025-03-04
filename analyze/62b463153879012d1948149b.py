def match_file_by_prefix(prefix, file_path):
    """
    Identifica si un `file_path` pertenece a un paquete de documentos según un `prefix` dado.

    Retorna `True` para documentos que pertenecen a un paquete.

    Parámetros
    ----------
    prefix : str  
    Prefijo del nombre del archivo.  

    file_path* : str  
    Ruta del archivo.  

    Retorna
    -------
    bool
    `True` - el archivo pertenece al paquete.  
    """
    # Get just the filename from the full path
    import os
    filename = os.path.basename(file_path)
    
    # Check if filename starts with the prefix
    return filename.startswith(prefix)
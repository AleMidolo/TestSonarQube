def match_file_by_prefix(prefix, file_path):
    """
    Identifica si un `file_path` pertenece a un paquete de documentos según un `prefix` dado.

    Retorna `True` para documentos que pertenecen a un paquete.

    Parámetros
    ----------
    prefix : str  
    Prefijo del nombre del archivo.  

    file_path : str  
    Ruta del archivo.  

    Retorna
    -------
    bool
    `True` - el archivo pertenece al paquete.  
    """
    import os
    file_name = os.path.basename(file_path)
    return file_name.startswith(prefix)
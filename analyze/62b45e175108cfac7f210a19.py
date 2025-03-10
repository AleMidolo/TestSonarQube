def validate_fixity(self, fixity, manifest_files):
    """
    Validar el bloque de fijación en el inventario.

    Verificar la estructura del bloque de fijación y asegurarse de que solo se referencien los archivos listados en el manifiesto.
    """
    if not isinstance(fixity, dict):
        raise ValueError("El bloque de fijación debe ser un diccionario.")
    
    if "files" not in fixity:
        raise ValueError("El bloque de fijación debe contener una clave 'files'.")
    
    if not isinstance(fixity["files"], dict):
        raise ValueError("La clave 'files' en el bloque de fijación debe ser un diccionario.")
    
    for file_name, checksum in fixity["files"].items():
        if file_name not in manifest_files:
            raise ValueError(f"El archivo '{file_name}' no está listado en el manifiesto.")
        
        if not isinstance(checksum, str):
            raise ValueError(f"El checksum para el archivo '{file_name}' debe ser una cadena de texto.")
    
    return True
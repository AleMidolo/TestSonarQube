def validate_fixity(self, fixity, manifest_files):
    """
    Validar el bloque de fijación en el inventario.

    Verificar la estructura del bloque de fijación y asegurarse de que solo se referencien los archivos listados en el manifiesto.
    """
    if not isinstance(fixity, dict):
        raise ValueError("El bloque de fijación debe ser un diccionario.")
    
    for file_name, checksum in fixity.items():
        if file_name not in manifest_files:
            raise ValueError(f"El archivo '{file_name}' no está listado en el manifiesto.")
        
        if not isinstance(checksum, str) or not checksum:
            raise ValueError(f"El checksum para el archivo '{file_name}' debe ser una cadena no vacía.")
    
    return True
def validate_fixity(self, fixity, manifest_files):
    """
    Validar el bloque de fijación en el inventario.

    Verificar la estructura del bloque de fijación y asegurarse de que solo se referencien los archivos listados en el manifiesto.

    Args:
        fixity (dict): El bloque de fijación que se va a validar.
        manifest_files (list): Lista de archivos listados en el manifiesto.

    Returns:
        bool: True si el bloque de fijación es válido, False en caso contrario.
    """
    if not isinstance(fixity, dict):
        return False
    
    for file_name, checksum in fixity.items():
        if file_name not in manifest_files:
            return False
    
    return True
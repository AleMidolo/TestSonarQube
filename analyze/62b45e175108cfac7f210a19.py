def validate_fixity(self, fixity, manifest_files):
    """
    Validar el bloque de fijación en el inventario.

    Verificar la estructura del bloque de fijación y asegurarse de que solo se referencien los archivos listados en el manifiesto.

    :param fixity: Diccionario que contiene el bloque de fijación.
    :param manifest_files: Lista de archivos listados en el manifiesto.
    :return: True si el bloque de fijación es válido, False en caso contrario.
    """
    if not isinstance(fixity, dict):
        return False
    
    for file_name, checksum in fixity.items():
        if file_name not in manifest_files:
            return False
    
    return True
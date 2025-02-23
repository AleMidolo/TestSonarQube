def validate_fixity(self, fixity, manifest_files):
    """
    Validar el bloque de fijación en el inventario.

    Verificar la estructura del bloque de fijación y asegurarse de que solo se referencien los archivos listados en el manifiesto.
    """
    # Verificar que el bloque de fijación sea un diccionario
    if not isinstance(fixity, dict):
        raise ValueError("El bloque de fijación debe ser un diccionario.")

    # Verificar que cada archivo en el bloque de fijación esté en el manifiesto
    manifest_set = set(manifest_files)
    for file in fixity.keys():
        if file not in manifest_set:
            raise ValueError(f"El archivo '{file}' no está en el manifiesto.")

    # Verificar que la estructura del bloque de fijación sea correcta
    for file, checksum in fixity.items():
        if not isinstance(checksum, str):
            raise ValueError(f"El checksum para el archivo '{file}' debe ser una cadena.")
    
    return True
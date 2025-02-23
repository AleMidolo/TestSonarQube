def validate_fixity(self, fixity, manifest_files):
    """
    Validar el bloque de fijación en el inventario.

    Verificar la estructura del bloque de fijación y asegurarse de que solo se referencien los archivos listados en el manifiesto.
    """
    # Verificar que el fixity sea un diccionario
    if not isinstance(fixity, dict):
        raise ValueError("El bloque de fijación debe ser un diccionario.")

    # Verificar que contenga las claves necesarias
    required_keys = ['file', 'checksum', 'algorithm']
    for key in required_keys:
        if key not in fixity:
            raise ValueError(f"Falta la clave requerida: {key}")

    # Verificar que el archivo referenciado esté en el manifiesto
    referenced_file = fixity['file']
    if referenced_file not in manifest_files:
        raise ValueError(f"El archivo referenciado '{referenced_file}' no está en el manifiesto.")

    # Verificar que el checksum y el algoritmo sean válidos
    if not isinstance(fixity['checksum'], str) or not fixity['checksum']:
        raise ValueError("El checksum debe ser una cadena no vacía.")
    
    if fixity['algorithm'] not in ['md5', 'sha1', 'sha256']:
        raise ValueError("El algoritmo debe ser uno de los siguientes: 'md5', 'sha1', 'sha256'.")

    return True
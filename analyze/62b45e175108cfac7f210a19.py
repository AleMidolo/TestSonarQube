def validate_fixity(self, fixity, manifest_files):
    """
    Validar el bloque de fijación en el inventario.

    Verificar la estructura del bloque de fijación y asegurarse de que solo se referencien los archivos listados en el manifiesto.
    """
    if not isinstance(fixity, dict):
        raise ValueError("El bloque de fijación debe ser un diccionario")

    # Verificar que tenga las claves requeridas
    required_keys = ["message_digest_algorithm", "message_digest"]
    for key in required_keys:
        if key not in fixity:
            raise ValueError(f"Falta la clave requerida '{key}' en el bloque de fijación")

    # Verificar que el algoritmo sea válido
    valid_algorithms = ["md5", "sha1", "sha256", "sha512"]
    if fixity["message_digest_algorithm"].lower() not in valid_algorithms:
        raise ValueError(f"Algoritmo de digest no válido. Debe ser uno de: {valid_algorithms}")

    # Verificar que los digests referencien archivos del manifiesto
    for file_path, digest in fixity["message_digest"].items():
        if file_path not in manifest_files:
            raise ValueError(f"El archivo '{file_path}' en el bloque de fijación no está presente en el manifiesto")
        
        if not isinstance(digest, str):
            raise ValueError(f"El digest para '{file_path}' debe ser una cadena")

    return True
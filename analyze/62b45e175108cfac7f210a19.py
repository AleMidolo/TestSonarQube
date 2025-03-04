def validate_fixity(self, fixity, manifest_files):
    """
    Validar el bloque de fijación en el inventario.
    
    Verificar la estructura del bloque de fijación y asegurarse de que solo se referencien los archivos listados en el manifiesto.
    """
    if not isinstance(fixity, dict):
        raise ValueError("El bloque de fijación debe ser un diccionario")
        
    # Verificar que tenga las claves requeridas
    required_keys = ['message_digest', 'algorithm']
    for key in required_keys:
        if key not in fixity:
            raise ValueError(f"Falta la clave requerida '{key}' en el bloque de fijación")
            
    # Verificar que el algoritmo sea válido
    valid_algorithms = ['md5', 'sha1', 'sha256', 'sha512']
    if fixity['algorithm'].lower() not in valid_algorithms:
        raise ValueError(f"Algoritmo de hash no válido. Debe ser uno de: {valid_algorithms}")
        
    # Verificar que los archivos referenciados existan en el manifiesto
    for file_hash in fixity['message_digest']:
        if not isinstance(file_hash, dict):
            raise ValueError("Cada entrada de message_digest debe ser un diccionario")
            
        if 'file' not in file_hash or 'hash' not in file_hash:
            raise ValueError("Las entradas de message_digest deben tener 'file' y 'hash'")
            
        if file_hash['file'] not in manifest_files:
            raise ValueError(f"El archivo {file_hash['file']} no está en el manifiesto")
            
        # Verificar que el hash tenga el formato correcto según el algoritmo
        hash_length = {
            'md5': 32,
            'sha1': 40, 
            'sha256': 64,
            'sha512': 128
        }
        
        expected_length = hash_length[fixity['algorithm'].lower()]
        if len(file_hash['hash']) != expected_length:
            raise ValueError(f"El hash para {file_hash['file']} no tiene la longitud correcta para {fixity['algorithm']}")
            
    return True
def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    """
    Validar la jerarquía de la raíz de almacenamiento.

    Retorna:
        num_objects - número de objetos verificados
        good_objects - número de objetos verificados que se encontraron válidos
    """
    num_objects = 0
    good_objects = 0

    # Recorrer recursivamente la jerarquía
    for root, dirs, files in os.walk(self.root_path):
        for file in files:
            num_objects += 1
            file_path = os.path.join(root, file)
            
            is_valid = True
            
            # Validar objeto si está habilitado
            if validate_objects:
                try:
                    with open(file_path, 'rb') as f:
                        content = f.read()
                        
                    # Verificar digest si está habilitado
                    if check_digests:
                        stored_digest = self._get_stored_digest(file_path)
                        calculated_digest = hashlib.sha256(content).hexdigest()
                        
                        if stored_digest != calculated_digest:
                            is_valid = False
                            if show_warnings:
                                print(f"Warning: Invalid digest for {file_path}")
                                
                except Exception as e:
                    is_valid = False
                    if show_warnings:
                        print(f"Warning: Error validating {file_path}: {str(e)}")
            
            if is_valid:
                good_objects += 1
                
    return num_objects, good_objects
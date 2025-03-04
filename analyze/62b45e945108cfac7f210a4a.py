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
    for root, dirs, files in self.walk():
        for file in files:
            num_objects += 1
            
            try:
                # Validar objeto si está habilitado
                if validate_objects:
                    obj = self.get_object(file)
                    
                    # Verificar digests si está habilitado
                    if check_digests:
                        if obj.verify_digest():
                            good_objects += 1
                        elif show_warnings:
                            print(f"Warning: Invalid digest for {file}")
                    else:
                        good_objects += 1
                        
            except Exception as e:
                if show_warnings:
                    print(f"Warning: Error validating {file}: {str(e)}")
                continue
                
    return num_objects, good_objects
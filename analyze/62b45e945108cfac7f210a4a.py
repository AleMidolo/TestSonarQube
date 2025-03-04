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
        
        # Validar cada objeto encontrado
        if validate_objects:
            for obj in files:
                num_objects += 1
                
                try:
                    # Verificar integridad del objeto
                    if check_digests:
                        if self.verify_object_digest(obj):
                            good_objects += 1
                    else:
                        if self.verify_object(obj):
                            good_objects += 1
                            
                except Exception as e:
                    if show_warnings:
                        print(f"Warning: Error validating object {obj}: {str(e)}")
                        
    return num_objects, good_objects
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

            # Validar objeto
            if validate_objects:
                try:
                    # Verificar que el archivo existe
                    if not os.path.exists(file_path):
                        if show_warnings:
                            print(f"Warning: File {file_path} does not exist")
                        continue

                    # Verificar permisos de lectura
                    if not os.access(file_path, os.R_OK):
                        if show_warnings:
                            print(f"Warning: No read permissions for {file_path}")
                        continue

                    # Verificar digest si está habilitado
                    if check_digests:
                        stored_digest = self.get_object_digest(file_path)
                        current_digest = self.calculate_digest(file_path)
                        
                        if stored_digest != current_digest:
                            if show_warnings:
                                print(f"Warning: Invalid digest for {file_path}")
                            continue

                    good_objects += 1

                except Exception as e:
                    if show_warnings:
                        print(f"Warning: Error validating {file_path}: {str(e)}")
                    continue

    return num_objects, good_objects
def was_processed(processed, path_name, verbose):
    # Expandir el nombre de la ruta a una ruta absoluta
    abs_path = os.path.abspath(path_name)
    
    # Verificar si la ruta ya está en el conjunto
    if abs_path in processed:
        if verbose:
            print(f"Warning: {path_name} already processed")
        return True
        
    # Si no está en el conjunto, agregarla y devolver False
    processed.add(abs_path)
    return False
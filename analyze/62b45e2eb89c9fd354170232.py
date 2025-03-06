def next_version(version):
    """
    El identificador de la siguiente versión debe seguir el patrón existente.

    Debe manejar tanto versiones con prefijo de ceros como versiones sin prefijo de ceros.
    """
    # Split the version into parts
    parts = version.split('.')
    
    # Convert each part to an integer
    parts = [int(part) for part in parts]
    
    # Increment the last part
    parts[-1] += 1
    
    # Handle carry-over
    for i in range(len(parts) - 1, 0, -1):
        if parts[i] > 9:
            parts[i] = 0
            parts[i - 1] += 1
    
    # Convert back to string with leading zeros if necessary
    next_version_str = '.'.join(f"{part:0{len(str(part))}}" for part in parts)
    
    return next_version_str
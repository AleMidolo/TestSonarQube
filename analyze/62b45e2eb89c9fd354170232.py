def next_version(version):
    """
    El identificador de la siguiente versión debe seguir el patrón existente.

    Debe manejar tanto versiones con prefijo de ceros como versiones sin prefijo de ceros.
    """
    # Split the version into parts
    parts = version.split('.')
    
    # Increment the last part
    last_part = int(parts[-1]) + 1
    parts[-1] = str(last_part)
    
    # Handle carry-over if necessary
    for i in range(len(parts) - 1, 0, -1):
        if int(parts[i]) > 9:
            parts[i] = '0'
            parts[i-1] = str(int(parts[i-1]) + 1)
    
    # Handle the first part if it exceeds 9
    if int(parts[0]) > 9:
        parts[0] = '0'
        parts.insert(0, '1')
    
    # Reconstruct the version string
    return '.'.join(parts)
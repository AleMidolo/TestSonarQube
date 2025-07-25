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
    
    # Join the parts back together
    next_version = '.'.join(parts)
    
    return next_version
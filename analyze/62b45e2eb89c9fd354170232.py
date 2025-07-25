def next_version(version):
    """
    El identificador de la siguiente versión debe seguir el patrón existente.

    Debe manejar tanto versiones con prefijo de ceros como versiones sin prefijo de ceros.
    """
    # Split the version into parts
    parts = version.split('.')
    
    # Increment the last part
    last_part = int(parts[-1]) + 1
    
    # Handle leading zeros if any
    if parts[-1].startswith('0'):
        # Preserve the number of digits
        last_part_str = f"{last_part:0{len(parts[-1])}d}"
    else:
        last_part_str = str(last_part)
    
    # Update the last part
    parts[-1] = last_part_str
    
    # Join the parts back together
    return '.'.join(parts)
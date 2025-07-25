def next_version(version):
    """
    El identificador de la siguiente versión debe seguir el patrón existente.

    Debe manejar tanto versiones con prefijo de ceros como versiones sin prefijo de ceros.
    """
    # Split the version into parts
    parts = version.split('.')
    
    # Increment the last part
    last_part = int(parts[-1]) + 1
    
    # Handle the case where the last part overflows (e.g., 9 -> 10)
    carry = 0
    for i in range(len(parts) - 1, -1, -1):
        if i == len(parts) - 1:
            parts[i] = str(last_part)
        else:
            parts[i] = str(int(parts[i]) + carry)
        
        if int(parts[i]) > 9:
            parts[i] = '0'
            carry = 1
        else:
            carry = 0
    
    # If there's still a carry, prepend '1' to the parts
    if carry:
        parts.insert(0, '1')
    
    # Reconstruct the version string
    return '.'.join(parts)
def next_version(version):
    """
    El identificador de la siguiente versión debe seguir el patrón existente.

    Debe manejar tanto versiones con prefijo de ceros como versiones sin prefijo de ceros.
    """
    parts = version.split('.')
    for i in range(len(parts) - 1, -1, -1):
        if parts[i].isdigit():
            parts[i] = str(int(parts[i]) + 1)
            break
        else:
            parts[i] = '0'
    else:
        parts.append('1')
    
    return '.'.join(parts)
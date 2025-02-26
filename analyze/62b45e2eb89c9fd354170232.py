def next_version(version):
    """
    El identificador de la siguiente versión debe seguir el patrón existente.

    Debe manejar tanto versiones con prefijo de ceros como versiones sin prefijo de ceros.
    """
    parts = version.split('.')
    for i in reversed(range(len(parts))):
        if parts[i].isdigit():
            parts[i] = str(int(parts[i]) + 1)
            for j in range(i + 1, len(parts)):
                parts[j] = '0'
            break
    return '.'.join(parts)
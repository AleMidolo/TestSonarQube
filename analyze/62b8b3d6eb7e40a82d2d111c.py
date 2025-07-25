def _normalizeargs(sequence, output=None):
    """
    Normalizar argumentos de declaración

    Los argumentos de normalización pueden contener Declaraciones, tuplas o interfaces individuales.

    Cualquier cosa que no sean interfaces individuales o especificaciones de implementación será expandida.
    """
    normalized = []
    
    for item in sequence:
        if isinstance(item, (tuple, list)):
            normalized.extend(_normalizeargs(item, output))
        elif isinstance(item, str) or hasattr(item, '__interface__'):
            normalized.append(item)
        else:
            if output is not None:
                output.append(item)
            normalized.append(item.__class__)
    
    return normalized
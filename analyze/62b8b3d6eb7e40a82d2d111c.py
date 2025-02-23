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
            # Expand the item if it's not a valid interface or declaration
            normalized.append(str(item))
    
    if output is not None:
        output.extend(normalized)
    
    return normalized
def _normalizeargs(sequence, output=None):
    """
    Normalizar argumentos de declaración

    Los argumentos de normalización pueden contener Declaraciones, tuplas o interfaces individuales.

    Cualquier cosa que no sean interfaces individuales o especificaciones de implementación será expandida.
    """
    if output is None:
        output = []
        
    if not sequence:
        return output
        
    for item in sequence:
        if isinstance(item, (list, tuple)):
            _normalizeargs(item, output)
        else:
            output.append(item)
            
    return output
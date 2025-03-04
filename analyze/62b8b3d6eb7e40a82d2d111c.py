def _normalizeargs(sequence, output=None):
    """
    Normalizar argumentos de declaración

    Los argumentos de normalización pueden contener Declaraciones, tuplas o interfaces individuales.

    Cualquier cosa que no sean interfaces individuales o especificaciones de implementación será expandida.
    """
    if output is None:
        output = []
    
    # Handle different types of input sequences
    if not sequence:
        return output
        
    # Handle single items
    if not hasattr(sequence, '__iter__') or isinstance(sequence, str):
        output.append(sequence)
        return output
        
    # Recursively process sequences
    for item in sequence:
        if isinstance(item, (list, tuple)):
            _normalizeargs(item, output)
        else:
            output.append(item)
            
    return output
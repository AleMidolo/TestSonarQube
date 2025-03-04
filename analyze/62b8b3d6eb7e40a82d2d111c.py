def _normalizeargs(sequence, output=None):
    if output is None:
        output = []
        
    if not sequence:
        return output
        
    # Handle single item
    if not hasattr(sequence, '__iter__') or isinstance(sequence, str):
        output.append(sequence)
        return output
        
    # Recursively normalize nested sequences
    for item in sequence:
        if isinstance(item, (list, tuple)):
            _normalizeargs(item, output)
        else:
            output.append(item)
            
    return output
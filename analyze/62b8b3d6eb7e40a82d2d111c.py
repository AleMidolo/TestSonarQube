def _normalizeargs(sequence, output=None):
    if output is None:
        output = []
    
    for item in sequence:
        if isinstance(item, tuple):
            output.extend(_normalizeargs(item))
        elif isinstance(item, list):
            output.extend(_normalizeargs(item))
        elif isinstance(item, dict):
            output.extend(_normalizeargs(item.values()))
        else:
            output.append(item)
    
    return output
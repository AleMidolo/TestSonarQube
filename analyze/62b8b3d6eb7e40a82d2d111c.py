def _normalizeargs(sequence, output=None):
    """
    Normalize declaration arguments

    Normalization arguments might contain Declarions, tuples, or single
    interfaces.

    Anything but individual interfaces or implements specs will be expanded.
    """
    if output is None:
        output = []
    
    for item in sequence:
        if isinstance(item, (tuple, list)):
            _normalizeargs(item, output)
        else:
            output.append(item)
    
    return output
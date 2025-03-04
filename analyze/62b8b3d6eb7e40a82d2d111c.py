def _normalizeargs(sequence, output=None):
    """
    Normalize declaration arguments

    Normalization arguments might contain Declarions, tuples, or single
    interfaces.

    Anything but individial interfaces or implements specs will be expanded.
    """
    if output is None:
        output = []
        
    for arg in sequence:
        if isinstance(arg, (list, tuple)):
            _normalizeargs(arg, output)
        elif hasattr(arg, 'interfaces'):
            _normalizeargs(arg.interfaces, output)
        else:
            output.append(arg)
            
    return output
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
            # If arg is a Declaration, expand its interfaces
            _normalizeargs(arg.interfaces, output)
        else:
            # Single interface or implements spec
            if arg not in output:
                output.append(arg)
                
    return output
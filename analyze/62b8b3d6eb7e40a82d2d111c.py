def _normalizeargs(sequence, output=None):
    """
    Normalize declaration arguments

    Normalization arguments might contain Declarions, tuples, or single
    interfaces.

    Anything but individial interfaces or implements specs will be expanded.
    """
    if output is None:
        output = []

    for item in sequence:
        if isinstance(item, (tuple, list)):
            output.extend(_normalizeargs(item))
        elif isinstance(item, str) and item not in output:
            output.append(item)
        # Assuming Declarions is a class or type we need to handle
        elif isinstance(item, Declarion) and item not in output:
            output.append(item)
    
    return output
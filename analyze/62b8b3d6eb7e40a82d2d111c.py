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
        if isinstance(item, tuple):
            output.extend(_normalizeargs(item))
        elif isinstance(item, list):
            output.extend(_normalizeargs(item))
        elif isinstance(item, str) or isinstance(item, int):
            output.append(item)
        else:
            output.append(str(item))

    return output
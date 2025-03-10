def size_to_bytes(size: str) -> int:
    """
    Convert human readable file size to bytes.

    Resulting value is an approximation as input value is in most case rounded.

    Args:
        size: A string representing a human readable file size (eg: '500K')

    Returns:
        A decimal representation of file size

    Examples::
        >>> size_to_bytes("500")
        500
        >>> size_to_bytes("1K")
        1000
    """
    size = size.strip().upper()
    if size[-1] == 'K':
        return int(size[:-1]) * 1000
    elif size[-1] == 'M':
        return int(size[:-1]) * 1000 * 1000
    elif size[-1] == 'G':
        return int(size[:-1]) * 1000 * 1000 * 1000
    elif size[-1] == 'T':
        return int(size[:-1]) * 1000 * 1000 * 1000 * 1000
    else:
        return int(size)
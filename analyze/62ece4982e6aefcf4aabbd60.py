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
    if size[-1] not in ['K', 'M', 'G', 'T', 'P']:
        return int(size)
    
    unit = size[-1]
    num = float(size[:-1])
    
    if unit == 'K':
        return int(num * 10**3)
    elif unit == 'M':
        return int(num * 10**6)
    elif unit == 'G':
        return int(num * 10**9)
    elif unit == 'T':
        return int(num * 10**12)
    elif unit == 'P':
        return int(num * 10**15)
    else:
        raise ValueError(f"Invalid size unit: {unit}")
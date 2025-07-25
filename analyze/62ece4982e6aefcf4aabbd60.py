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
    units = {
        'K': 1000,
        'M': 1000000,
        'G': 1000000000,
        'T': 1000000000000,
    }

    size = size.strip().upper()
    
    if size[-1] in units:
        number = float(size[:-1])
        unit = size[-1]
        return int(number * units[unit])
    else:
        return int(size)
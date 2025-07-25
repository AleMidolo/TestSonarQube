def size_to_bytes(size: str) -> int:
    """
    Convertire una dimensione di file leggibile dall'uomo in byte.

    Il valore risultante è un'approssimazione poiché il valore di input è nella maggior parte dei casi arrotondato.

    Args:
        size: Una stringa che rappresenta una dimensione di file leggibile dall'uomo (es: '500K')

    Returns:
        Una rappresentazione decimale della dimensione del file

    Esempi::

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
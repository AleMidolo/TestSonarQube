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
    if size[-1] in ['K', 'M', 'G', 'T']:
        num = float(size[:-1])
        unit = size[-1]
        if unit == 'K':
            return int(num * 1000)
        elif unit == 'M':
            return int(num * 1000 ** 2)
        elif unit == 'G':
            return int(num * 1000 ** 3)
        elif unit == 'T':
            return int(num * 1000 ** 4)
    else:
        return int(size)
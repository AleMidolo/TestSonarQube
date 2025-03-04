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
    multipliers = {
        'K': 1000,
        'M': 1000**2,
        'G': 1000**3,
        'T': 1000**4,
        'P': 1000**5,
        'E': 1000**6,
    }
    
    if size[-1] in multipliers:
        number = float(size[:-1])
        return int(number * multipliers[size[-1]])
    else:
        return int(size)
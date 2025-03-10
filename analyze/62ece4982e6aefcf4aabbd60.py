def size_to_bytes(size: str) -> int:
    """
    Convertir tamaño de archivo legible por humanos a bytes.

    El valor resultante es una aproximación, ya que el valor de entrada en la mayoría de los casos está redondeado.

    Args:
        size: Una cadena que representa un tamaño de archivo legible por humanos (por ejemplo: '500K')

    Returns:
        Una representación decimal del tamaño del archivo

    Ejemplos::

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
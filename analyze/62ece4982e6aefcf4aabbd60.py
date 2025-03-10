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
    if size[-1] not in ['K', 'M', 'G', 'T']:
        return int(size)
    
    unit = size[-1]
    num = float(size[:-1])
    
    if unit == 'K':
        return int(num * 1000)
    elif unit == 'M':
        return int(num * 1000 ** 2)
    elif unit == 'G':
        return int(num * 1000 ** 3)
    elif unit == 'T':
        return int(num * 1000 ** 4)
    else:
        raise ValueError(f"Unidad no reconocida: {unit}")
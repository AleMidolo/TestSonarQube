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
    multipliers = {
        'B': 1,
        'K': 1000,
        'M': 1000000,
        'G': 1000000000,
        'T': 1000000000000,
    }
    
    if size[-1] in multipliers:
        number = float(size[:-1])
        unit = size[-1]
    else:
        number = float(size)
        unit = 'B'
    
    return int(number * multipliers[unit])
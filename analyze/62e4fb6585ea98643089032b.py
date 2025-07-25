def parse_version(s: str) -> tuple[int, ...]:
    """
    Comparación de versiones rudimentaria.
    Convierte una cadena de versión en una tupla de enteros para facilitar la comparación.
    
    Args:
        s (str): Cadena de versión en formato "X.Y.Z..." donde X, Y, Z son números enteros.
    
    Returns:
        tuple[int, ...]: Tupla de enteros representando la versión.
    """
    return tuple(map(int, s.split('.')))
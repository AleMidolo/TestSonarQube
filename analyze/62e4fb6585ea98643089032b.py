def parse_version(s: str) -> tuple[int, ...]:
    """
    Comparación de versiones rudimentaria.
    Convierte una cadena de versión en una tupla de enteros.
    
    Args:
        s (str): Cadena de versión en formato "X.Y.Z" o similar.
    
    Returns:
        tuple[int, ...]: Tupla de enteros representando la versión.
    """
    return tuple(map(int, s.split('.')))
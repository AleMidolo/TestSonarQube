def parse_version(s: str) -> tuple[int, ...]:
    """
    Comparación de versiones rudimentaria.
    Convierte una cadena de versión en una tupla de enteros.
    
    Args:
        s (str): Cadena de versión, por ejemplo "1.2.3".
    
    Returns:
        tuple[int, ...]: Tupla de enteros representando la versión, por ejemplo (1, 2, 3).
    """
    return tuple(map(int, s.split('.')))
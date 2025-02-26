def parse_version(s: str) -> tuple[int, ...]:
    """
    comparación de versiones rudimentaria
    """
    return tuple(map(int, s.split('.')))
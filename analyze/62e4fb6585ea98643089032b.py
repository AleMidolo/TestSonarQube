def parse_version(s: str) -> tuple[int, ...]:
    """
    comparación de versiones rudimentaria
    """
    # Split version string by dots and convert each part to integer
    return tuple(int(x) for x in s.split('.'))
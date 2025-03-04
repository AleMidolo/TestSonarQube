def parse_version(s: str) -> tuple[int, ...]:
    """versione semplificata per il confronto delle versioni"""
    # Split version string by dots and convert each part to integer
    return tuple(int(x) for x in s.split('.'))
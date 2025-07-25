def parse_version(s: str) -> tuple[int, ...]:
    """versione semplificata per il confronto delle versioni"""
    return tuple(map(int, s.split('.')))
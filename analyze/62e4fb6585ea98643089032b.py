def parse_version(s: str) -> tuple[int, ...]:
    """versione semplificata per il confronto delle versioni"""
    return tuple(int(part) for part in s.split('.'))
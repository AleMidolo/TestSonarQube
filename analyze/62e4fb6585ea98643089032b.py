def parse_version(s: str) -> tuple[int, ...]:
    """
    poor man's version comparison
    """
    return tuple(int(part) for part in s.split('.'))
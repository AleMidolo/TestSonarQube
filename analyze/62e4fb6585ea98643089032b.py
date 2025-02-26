def parse_version(s: str) -> tuple[int, ...]:
    """
    साधारण (poor man's) वर्शन तुलना।
    """
    return tuple(map(int, s.split('.')))
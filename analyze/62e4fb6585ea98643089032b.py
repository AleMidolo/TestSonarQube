def parse_version(s: str) -> tuple[int, ...]:
    """
    poor man's version comparison
    """
    # Split version string on dots and convert each part to int
    return tuple(int(x) for x in s.split('.'))
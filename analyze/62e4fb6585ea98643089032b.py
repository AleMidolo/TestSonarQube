def parse_version(s: str) -> tuple[int, ...]:
    """
    साधारण (poor man's) वर्शन तुलना।
    """
    # Split version string by dots and convert each part to integer
    return tuple(int(x) for x in s.split('.'))
def parse_version(s: str) -> tuple[int, ...]:
    """
    Parses a version string into a tuple of integers for simplified version comparison.

    Args:
        s (str): The version string to parse.

    Returns:
        tuple[int, ...]: A tuple of integers representing the version.
    """
    return tuple(map(int, s.split('.')))
def parse_version(s: str) -> tuple[int, ...]:
    """
    साधारण (poor man's) वर्शन तुलना।
    
    Args:
        s (str): A version string, e.g., "1.2.3".
    
    Returns:
        tuple[int, ...]: A tuple of integers representing the version parts.
    """
    return tuple(map(int, s.split('.')))
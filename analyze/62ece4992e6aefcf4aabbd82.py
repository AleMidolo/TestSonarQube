import re

def get_pattern(pattern, strip=True):
    """
    This method converts the given string to regex pattern.
    
    Args:
        pattern (str): The string to be converted to a regex pattern.
        strip (bool): If True, strips leading and trailing whitespace from the pattern.
    
    Returns:
        re.Pattern: The compiled regex pattern.
    """
    if strip:
        pattern = pattern.strip()
    return re.compile(pattern)
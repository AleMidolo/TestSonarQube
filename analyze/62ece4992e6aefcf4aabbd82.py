def get_pattern(pattern, strip=True):
    """
    This method converts the given string to regex pattern
    """
    import re
    
    if strip:
        pattern = pattern.strip()
    
    # Escape special characters in the pattern
    escaped_pattern = re.escape(pattern)
    
    # Return the regex pattern
    return f"^{escaped_pattern}$"
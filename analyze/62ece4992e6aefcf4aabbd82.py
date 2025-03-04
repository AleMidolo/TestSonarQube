def get_pattern(pattern, strip=True):
    """
    This method converts the given string to regex pattern
    """
    # Escape special regex characters
    special_chars = ['\\', '^', '$', '.', '|', '?', '*', '+', '(', ')', '[', ']', '{', '}']
    
    # If strip is True, remove leading/trailing whitespace
    if strip:
        pattern = pattern.strip()
        
    # Escape special characters by adding backslash
    for char in special_chars:
        pattern = pattern.replace(char, '\\' + char)
        
    # Return the escaped pattern string
    return pattern
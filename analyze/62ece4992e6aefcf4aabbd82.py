def get_pattern(pattern, strip=True):
    """
    यह मेथड दी गई स्ट्रिंग को रेगुलर एक्सप्रेशन (Regex) पैटर्न में बदलता है।
    """
    # Special characters in regex that need to be escaped
    special_chars = '.^$*+?{}[]\\|()'
    
    # Strip whitespace if strip=True
    if strip:
        pattern = pattern.strip()
    
    # Escape special regex characters
    escaped_pattern = ''
    for char in pattern:
        if char in special_chars:
            escaped_pattern += '\\' + char
        else:
            escaped_pattern += char
            
    return escaped_pattern
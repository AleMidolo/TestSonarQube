def get_pattern(pattern, strip=True):
    """
    Este método convierte la cadena proporcionada en un objeto de patrón regex.
    """
    import re
    
    if strip:
        pattern = pattern.strip()
        
    try:
        return re.compile(pattern)
    except re.error:
        return None
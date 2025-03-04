def get_pattern(pattern, strip=True):
    """
    Questo metodo converte la stringa fornita in un oggetto pattern regex
    """
    import re
    
    if strip:
        pattern = pattern.strip()
        
    try:
        return re.compile(pattern)
    except re.error:
        return None
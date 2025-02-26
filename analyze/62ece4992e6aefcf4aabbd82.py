import re

def get_pattern(pattern, strip=True):
    """
    Este método convierte la cadena proporcionada en un objeto de patrón regex.
    """
    if strip:
        pattern = pattern.strip()
    return re.compile(pattern)
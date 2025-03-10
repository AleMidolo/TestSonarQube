import re

def get_pattern(pattern, strip=True):
    """
    Este método convierte la cadena proporcionada en un objeto de patrón regex.
    
    Args:
        pattern (str): La cadena que se convertirá en un patrón regex.
        strip (bool): Si es True, elimina los espacios en blanco al principio y al final de la cadena.
    
    Returns:
        re.Pattern: El objeto de patrón regex compilado.
    """
    if strip:
        pattern = pattern.strip()
    return re.compile(pattern)
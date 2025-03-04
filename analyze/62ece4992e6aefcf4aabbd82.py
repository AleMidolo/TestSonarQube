import re

def get_pattern(pattern, strip=True):
    """
    Questo metodo converte la stringa fornita in un oggetto pattern regex
    """
    if strip:
        pattern = pattern.strip()
    return re.compile(pattern)
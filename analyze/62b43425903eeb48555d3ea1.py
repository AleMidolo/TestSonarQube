import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    """
    Crea l'espressione regolare per il parametro in-style.

    Restituisce l'espressione regolare per il parametro in-style (:class:`re.Pattern`).
    """
    # Example regex pattern for in-style parameter
    pattern = r'\b(?:in|not in)\s+\w+\b'
    return re.compile(pattern)
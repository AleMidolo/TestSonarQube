import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    """
    Crea la expresión regular del parámetro "in-style".

        Devuelve la expresión regular para el parámetro "in-style" (:class:`re.Pattern`).
    """
    # Define the regex pattern for "in-style"
    pattern = r'in-style:\s*([a-zA-Z0-9_-]+)'
    return re.compile(pattern)
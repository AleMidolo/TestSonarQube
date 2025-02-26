import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    """
    Crea la expresión regular del parámetro "in-style".

        Devuelve la expresión regular para el parámetro "in-style" (:class:`re.Pattern`).
    """
    # Ejemplo de expresión regular para "in-style"
    return re.compile(r'in-style:\s*([a-zA-Z0-9_-]+)')
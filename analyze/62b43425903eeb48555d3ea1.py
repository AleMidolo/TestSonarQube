import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    """
    Crea la expresión regular del parámetro "in-style".

        Devuelve la expresión regular para el parámetro "in-style" (:class:`re.Pattern`).
    """
    # Definición de la expresión regular para "in-style"
    regex_pattern = r'in-style'  # Aquí se puede ajustar la expresión regular según sea necesario
    return re.compile(regex_pattern)
import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    """
    Crea la expresión regular del parámetro "in-style".

    Devuelve la expresión regular para el parámetro "in-style" (:class:`re.Pattern`).
    """
    # Definición de la expresión regular para el estilo "in"
    regex_pattern = r'in-style'  # Ajustar el patrón según sea necesario
    return re.compile(regex_pattern)
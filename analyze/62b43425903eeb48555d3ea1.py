import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    """
    Crea la expresión regular del parámetro "in-style".

        Devuelve la expresión regular para el parámetro "in-style" (:class:`re.Pattern`).
    """
    # Aquí se define la expresión regular para el estilo "in"
    regex_pattern = r'in-style'  # Ejemplo de patrón, debe ser ajustado según la necesidad
    return re.compile(regex_pattern)
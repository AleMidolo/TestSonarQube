import re

def _create_in_regex(self) -> Pattern:
    """
    Crea la expresión regular del parámetro "in-style".

    Devuelve la expresión regular para el parámetro "in-style" (:class:`re.Pattern`).
    """
    # Define the regex pattern for "in-style" parameter
    pattern = r"in\s*\(([^)]+)\)"
    return re.compile(pattern)
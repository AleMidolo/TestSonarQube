def _create_in_regex(self) -> Pattern:
    """
    Crea la expresión regular del parámetro "in-style".

    Devuelve la expresión regular para el parámetro "in-style" (:class:`re.Pattern`).
    """
    import re
    pattern = r'in-style\s*=\s*["\']([^"\']+)["\']'
    return re.compile(pattern)
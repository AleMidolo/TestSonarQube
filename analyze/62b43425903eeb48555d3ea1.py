import re

def _create_in_regex(self) -> Pattern:
    """
    Crea l'espressione regolare per il parametro in-style.

    Restituisce l'espressione regolare per il parametro in-style (:class:`re.Pattern`).
    """
    return re.compile(r':in\b')
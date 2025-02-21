import re

class ValidationError(Exception):
    pass

def validate_key(key):
    """
    Valida la chiave fornita rispetto alla corrispondente espressione regolare.

    Argomenti:
        key: la stringa da validare

    Eccezioni:
        ValidationError: se la chiave fornita non è conforme all'espressione regolare.
    """
    pattern = r'^[A-Za-z0-9]{8,}$'  # esempio di espressione regolare
    if not re.match(pattern, key):
        raise ValidationError("La chiave fornita non è conforme all'espressione regolare.")
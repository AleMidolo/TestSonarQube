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
    pattern = r'^[A-Z0-9]{8}$'  # esempio di espressione regolare per una chiave di 8 caratteri alfanumerici
    if not re.match(pattern, key):
        raise ValidationError("La chiave fornita non è conforme all'espressione regolare.")
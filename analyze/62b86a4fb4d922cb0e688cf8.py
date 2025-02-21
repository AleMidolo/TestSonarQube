import re

class ValidationError(Exception):
    pass

def validate_value(value):
    """
    Convalida il valore fornito rispetto alla corrispondente espressione regolare.

    Argomenti:
        value: la stringa da convalidare

    Eccezioni:
        ValidationError: se il valore fornito non è conforme all'espressione regolare.
    """
    pattern = r'^[a-zA-Z0-9]+$'  # Esempio di espressione regolare
    if not re.match(pattern, value):
        raise ValidationError(f"Il valore '{value}' non è conforme all'espressione regolare.")
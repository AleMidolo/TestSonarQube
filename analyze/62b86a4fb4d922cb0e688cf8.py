import re

def validate_value(value):
    """
    Convalida il valore fornito rispetto alla corrispondente espressione regolare.

    Argomenti:
        value: la stringa da convalidare

    Eccezioni:
        ValidationError: se il valore fornito non è conforme all'espressione regolare.
    """
    # Definisci l'espressione regolare per la convalida
    pattern = r'^[A-Za-z0-9]+$'  # Esempio: solo lettere e numeri
    
    if not re.match(pattern, value):
        raise ValidationError("Il valore fornito non è conforme all'espressione regolare.")
    
    return True

class ValidationError(Exception):
    """Eccezione sollevata quando il valore non è conforme all'espressione regolare."""
    pass
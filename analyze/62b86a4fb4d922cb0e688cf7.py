import re

def validate_key(key):
    """
    Valida la chiave fornita rispetto alla corrispondente espressione regolare.

    Argomenti:
        key: la stringa da validare

    Eccezioni:
        ValidationError: se la chiave fornita non è conforme all'espressione regolare.
    """
    # Definisci l'espressione regolare per la validazione della chiave
    pattern = r'^[A-Za-z0-9_\-]+$'  # Esempio: solo lettere, numeri, underscore e trattini
    
    if not re.match(pattern, key):
        raise ValidationError("La chiave fornita non è conforme all'espressione regolare.")
    
    return True

class ValidationError(Exception):
    """Eccezione sollevata quando la validazione fallisce."""
    pass
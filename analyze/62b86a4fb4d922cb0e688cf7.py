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
    # Esempio: la chiave deve essere composta da lettere minuscole e numeri, lunghezza 8-16 caratteri
    pattern = re.compile(r'^[a-z0-9]{8,16}$')
    
    if not pattern.match(key):
        raise ValidationError("La chiave fornita non è conforme all'espressione regolare.")
    
    return True

class ValidationError(Exception):
    """Eccezione sollevata quando la validazione fallisce."""
    pass
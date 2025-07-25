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
    # Esempio: accetta solo stringhe alfanumeriche con lunghezza tra 3 e 20 caratteri
    regex = re.compile(r'^[a-zA-Z0-9]{3,20}$')
    
    if not regex.match(value):
        raise ValidationError("Il valore fornito non è conforme all'espressione regolare.")
    
    return True

class ValidationError(Exception):
    """Eccezione sollevata quando il valore non è conforme all'espressione regolare."""
    pass
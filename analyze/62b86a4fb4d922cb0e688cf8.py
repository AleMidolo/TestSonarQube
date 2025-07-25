def validate_value(value):
    """
    Convalida il valore fornito rispetto alla corrispondente espressione regolare.

    Argomenti:
        value: la stringa da convalidare

    Eccezioni:
        ValidationError: se il valore fornito non è conforme all'espressione regolare.
    """
    import re

    # Pattern per validare che la stringa contenga solo lettere, numeri e underscore
    pattern = r'^[a-zA-Z0-9_]+$'
    
    # Verifica se il valore è una stringa
    if not isinstance(value, str):
        raise ValidationError("Il valore deve essere una stringa")
        
    # Verifica se la stringa è vuota
    if not value:
        raise ValidationError("Il valore non può essere vuoto")
        
    # Verifica se la stringa corrisponde al pattern
    if not re.match(pattern, value):
        raise ValidationError("Il valore contiene caratteri non validi")
        
    return True

class ValidationError(Exception):
    """Eccezione sollevata per errori di validazione"""
    pass
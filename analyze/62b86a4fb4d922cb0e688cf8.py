import re

def validate_value(value):
    """
    Validar el valor proporcionado contra la expresión regular correspondiente.

    Argumentos:
        value: la cadena de texto a validar

    Excepciones:
        ValidationError: si el valor proporcionado no cumple con la expresión regular.
    """
    # Expresión regular para validar (puedes cambiarla según tus necesidades)
    regex_pattern = r'^[A-Za-z0-9_]+$'
    
    if not re.match(regex_pattern, value):
        raise ValidationError("El valor proporcionado no cumple con la expresión regular.")
    
    return True

class ValidationError(Exception):
    """Excepción personalizada para errores de validación."""
    pass
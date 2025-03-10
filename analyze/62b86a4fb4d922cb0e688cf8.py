import re

def validate_value(value):
    """
    Validar el valor proporcionado contra la expresión regular correspondiente.

    Argumentos:
        value: la cadena de texto a validar

    Excepciones:
        ValidationError: si el valor proporcionado no cumple con la expresión regular.
    """
    # Expresión regular para validar que el valor sea una cadena alfanumérica
    regex = r'^[a-zA-Z0-9]+$'
    
    if not re.match(regex, value):
        raise ValidationError("El valor proporcionado no cumple con la expresión regular.")
    
    return True

class ValidationError(Exception):
    """Excepción personalizada para errores de validación."""
    pass
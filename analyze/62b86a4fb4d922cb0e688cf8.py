import re

class ValidationError(Exception):
    pass

def validate_value(value):
    """
    Validar el valor proporcionado contra la expresión regular correspondiente.

    Argumentos:
        value: la cadena de texto a validar

    Excepciones:
        ValidationError: si el valor proporcionado no cumple con la expresión regular.
    """
    pattern = r'^[a-zA-Z0-9_]+$'  # Example pattern: alphanumeric and underscores
    if not re.match(pattern, value):
        raise ValidationError(f"El valor '{value}' no cumple con la expresión regular.")
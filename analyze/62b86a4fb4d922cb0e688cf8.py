import re

def validate_value(value):
    """
    Validar el valor proporcionado contra la expresión regular correspondiente.

    Argumentos:
        value: la cadena de texto a validar

    Excepciones:
        ValidationError: si el valor proporcionado no cumple con la expresión regular.
    """
    # Define la expresión regular que debe cumplir el valor
    regex_pattern = r'^[A-Za-z0-9_]+$'  # Ejemplo: solo letras, números y guiones bajos
    
    if not re.match(regex_pattern, value):
        raise ValidationError(f"El valor '{value}' no cumple con la expresión regular.")
    
    return True

class ValidationError(Exception):
    """Excepción personalizada para errores de validación."""
    pass
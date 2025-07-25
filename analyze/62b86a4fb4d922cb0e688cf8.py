def validate_value(value):
    """
    Validar el valor proporcionado contra la expresión regular correspondiente.

    Argumentos:
        value: la cadena de texto a validar

    Excepciones:
        ValidationError: si el valor proporcionado no cumple con la expresión regular.
    """
    import re

    # Expresión regular para validar que el valor solo contenga letras, números y espacios
    pattern = r'^[a-zA-Z0-9\s]+$'

    # Validar que el valor no esté vacío
    if not value:
        raise ValidationError("El valor no puede estar vacío")

    # Validar que el valor sea una cadena de texto
    if not isinstance(value, str):
        raise ValidationError("El valor debe ser una cadena de texto")

    # Validar que el valor cumpla con la expresión regular
    if not re.match(pattern, value):
        raise ValidationError("El valor solo puede contener letras, números y espacios")

    return True

class ValidationError(Exception):
    """Excepción personalizada para errores de validación"""
    pass
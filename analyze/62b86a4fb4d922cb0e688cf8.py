def validate_value(value):
    """
    Validar el valor proporcionado contra la expresión regular correspondiente.

    Argumentos:
        value: la cadena de texto a validar

    Excepciones:
        ValidationError: si el valor proporcionado no cumple con la expresión regular.
    """
    import re

    # Expresión regular para validar:
    # - Al menos una letra mayúscula
    # - Al menos una letra minúscula 
    # - Al menos un número
    # - Al menos un carácter especial
    # - Longitud mínima de 8 caracteres
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    if not isinstance(value, str):
        raise ValidationError("El valor debe ser una cadena de texto")

    if not re.match(pattern, value):
        raise ValidationError("El valor no cumple con los requisitos de validación")

    return True

class ValidationError(Exception):
    """Excepción personalizada para errores de validación"""
    pass
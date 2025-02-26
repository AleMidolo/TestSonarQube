import re

class ValidationError(Exception):
    pass

def validate_key(key):
    """
    Validar la clave proporcionada contra la expresión regular correspondiente.

    Argumentos:
            key: la cadena de texto a validar.

    Excepciones:
            ValidationError: si la clave proporcionada no cumple con la expresión regular.
    """
    # Definir la expresión regular para la clave
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'  # Al menos 8 caracteres, al menos una letra y un número

    if not re.match(pattern, key):
        raise ValidationError("La clave proporcionada no cumple con los requisitos.")
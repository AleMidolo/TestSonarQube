def validate_key(key):
    """
    Validar la clave proporcionada contra la expresión regular correspondiente.

    Argumentos:
        key: la cadena de texto a validar.

    Excepciones:
        ValidationError: si la clave proporcionada no cumple con la expresión regular.
    """
    import re
    
    # Expresión regular para validar la clave
    # Debe contener al menos:
    # - 8 caracteres
    # - 1 letra mayúscula
    # - 1 letra minúscula  
    # - 1 número
    # - 1 caracter especial
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    if not re.match(pattern, key):
        raise ValidationError("La clave no cumple con los requisitos mínimos de seguridad")
        
    return True

class ValidationError(Exception):
    pass
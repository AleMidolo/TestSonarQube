def validate_phone_number(self, phone_number):
    """
    Verifica si el número de teléfono es válido
    :param phone_number: Número de teléfono a verificar
    :return: True o False, indicando si el número de teléfono es válido
    >>> ru = RegexUtils()
    >>> ru.validate_phone_number("123-456-7890")
    True
    """
    import re
    
    if not phone_number:
        return False
    
    # Pattern for phone numbers in format: XXX-XXX-XXXX
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    
    return bool(re.match(pattern, phone_number))
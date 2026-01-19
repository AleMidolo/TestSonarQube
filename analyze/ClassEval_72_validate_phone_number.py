def validate_phone_number(self, phone_number):
    """
    Verifica se il numero di telefono è valido
    :param phone_number: Numero di telefono da verificare
    :return: True o False, che indica se il numero di telefono è valido
    >>> ru = RegexUtils()
    >>> ru.validate_phone_number("123-456-7890")
    True
    """
    import re
    
    # Pattern for phone numbers in format: XXX-XXX-XXXX
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    
    if re.match(pattern, phone_number):
        return True
    return False
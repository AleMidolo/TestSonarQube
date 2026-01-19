def generate_phone_number_pattern(self):
    """
    Genera patrones de expresiones regulares que coinciden con números de teléfono
    :return: cadena, patrones de expresiones regulares que coinciden con números de teléfono
    >>> ru = RegexUtils()
    >>> ru.generate_phone_number_pattern()
    '\b\d{3}-\d{3}-\d{4}\b'
    """
    return r'\b\d{3}-\d{3}-\d{4}\b'
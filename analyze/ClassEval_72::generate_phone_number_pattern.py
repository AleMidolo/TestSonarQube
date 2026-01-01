def generate_phone_number_pattern(self):
    """
        Genera patrones de expresiones regulares que coinciden con números de teléfono
        :return: cadena, patrones de expresiones regulares que coinciden con números de teléfono
        >>> ru = RegexUtils()
        >>> ru.generate_phone_number_pattern()
        '\x08\\d{3}-\\d{3}-\\d{4}\x08'
        """
    pattern = '\\b\\d{3}-\\d{3}-\\d{4}\\b'
    return pattern
def generate_email_pattern(self):
    """
    Genera patrones de expresiones regulares que coinciden con direcciones de correo electrónico
    :return: cadena, patrones de expresiones regulares que coinciden con direcciones de correo electrónico
    >>> ru = RegexUtils()
    >>> ru.generate_email_pattern()
    '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    """
    return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def generate_phone_number_pattern(self):
    """
    Genera patterns di espressione regolare che corrispondono ai numeri di telefono
    :return: stringa, modelli di espressione regolare che corrispondono ai numeri di telefono
    >>> ru = RegexUtils()
    >>> ru.generate_phone_number_pattern()
    '\b\d{3}-\d{3}-\d{4}\b'
    """
    return r'\b\d{3}-\d{3}-\d{4}\b'
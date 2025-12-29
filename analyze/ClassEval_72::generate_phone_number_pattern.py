def generate_phone_number_pattern(self):
    """
        Genera patterns di espressione regolare che corrispondono ai numeri di telefono
        :return: stringa, modelli di espressione regolare che corrispondono ai numeri di telefono
        >>> ru = RegexUtils()
        >>> ru.generate_phone_number_pattern()
        '\x08\\d{3}-\\d{3}-\\d{4}\x08'
        """
    pattern = '\\b\\d{3}-\\d{3}-\\d{4}\\b'
    return pattern
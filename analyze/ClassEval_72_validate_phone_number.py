def validate_phone_number(self, phone_number):
    """
        Verifica si el número de teléfono es válido
        :param phone_number: Número de teléfono a verificar
        :return: True o False, indicando si el número de teléfono es válido
        >>> ru = RegexUtils()
        >>> ru.validate_phone_number("123-456-7890")
        True
        """
    pattern = self.generate_phone_number_pattern()
    return bool(re.fullmatch(pattern, phone_number))
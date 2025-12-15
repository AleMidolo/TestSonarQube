def validate_phone_number(self, phone_number):
    """
    Verifica se il numero di telefono è valido
    :param phone_number: Numero di telefono da verificare
    :return: True o False, che indica se il numero di telefono è valido
    >>> ru = RegexUtils()
    >>> ru.validate_phone_number("123-456-7890")
    True
    """
    pattern = self.generate_phone_number_pattern()
    return self.match(pattern, phone_number)
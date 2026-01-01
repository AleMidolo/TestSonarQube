@staticmethod
def decimal_to_octal(decimal_num):
    """
        Convertir un número del formato decimal al formato octal.
        :param decimal_num: int, número decimal
        :return: str, la representación octal de un entero.
        >>> NumberConverter.decimal_to_octal(42423)
        '122667'
        """
    octal_num = oct(decimal_num)[2:]
    return octal_num
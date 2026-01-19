@staticmethod
def decimal_to_hex(decimal_num):
    """
        Convierte un número del formato decimal al formato hexadecimal.
        :param decimal_num: int, número decimal
        :return hex_num: str, la representación hexadecimal de un entero.
        >>> NumberConverter.decimal_to_hex(42423)
        'a5b7'
        """
    hex_num = hex(decimal_num)[2:]
    return hex_num
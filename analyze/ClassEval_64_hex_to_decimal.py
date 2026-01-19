@staticmethod
def hex_to_decimal(hex_num):
    """
        Convertir un número del formato hexadecimal al formato decimal.
        :param hex_num: str, número hexadecimal
        :return: int, la representación decimal del número hexadecimal str.
        >>> NumberConverter.hex_to_decimal('a5b7')
        42423
        """
    decimal_num = int(hex_num, 16)
    return decimal_num
@staticmethod
def hex_to_decimal(hex_num):
    """
        Convert a number from hexadecimal format to decimal format.
        :param hex_num: str, hexadecimal number
        :return: int, the decimal representation of the hexadecimal number string.
        >>> NumberConverter.hex_to_decimal('a5b7')
        42423
        """
    decimal_num = int(hex_num, 16)
    return decimal_num
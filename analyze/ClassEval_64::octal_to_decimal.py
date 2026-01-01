@staticmethod
def octal_to_decimal(octal_num):
    """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal number
        :return: int, the decimal representation of octal number str.
        >>> NumberConverter.octal_to_decimal('122667')
        42423
        """
    decimal_num = int(octal_num, 8)
    return decimal_num
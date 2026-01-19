@staticmethod
def octal_to_decimal(octal_num):
    """
    Convert a number from octal format to decimal format.
    :param octal_num: str, octal num
    :return: int, the decimal representation of octal number str.
    >>> NumberConverter.octal_to_decimal('122667')
    42423
    """
    decimal = 0
    for i, digit in enumerate(reversed(octal_num)):
        decimal += int(digit) * (8 ** i)
    return decimal
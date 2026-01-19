@staticmethod
def octal_to_decimal(octal_num):
    """
    Convierte un número del formato octal al formato decimal.
    :param octal_num: str, número octal
    :return: int, la representación decimal del número octal como str.
    >>> NumberConverter.octal_to_decimal('122667')
    42423
    """
    return int(octal_num, 8)
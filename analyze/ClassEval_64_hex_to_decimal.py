@staticmethod
def hex_to_decimal(hex_num):
    """
    Converti un numero dal formato esadecimale al formato decimale.
    :param hex_num: str, numero esadecimale
    :return: int, la rappresentazione decimale della stringa del numero esadecimale.
    >>> NumberConverter.hex_to_decimal('a5b7')
    42423
    """
    return int(hex_num, 16)
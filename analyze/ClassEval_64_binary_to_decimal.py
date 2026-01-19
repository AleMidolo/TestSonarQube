@staticmethod
def binary_to_decimal(binary_num):
    """
    Converti un numero dal formato binario al formato decimale.
    :param binary_num: str, numero binario
    :return: int, la rappresentazione decimale del numero binario str.
    >>> NumberConverter.binary_to_decimal('1010010110110111')
    42423
    """
    return int(binary_num, 2)
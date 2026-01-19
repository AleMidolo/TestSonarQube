@staticmethod
def hex_to_decimal(hex_num):
    """
    Convert a number from hex format to decimal format.
    :param hex_num: str, hex num
    :return: int, the decimal representation of hex number str.
    >>> NumberConverter.hex_to_decimal('a5b7')
    42423
    """
    return int(hex_num, 16)
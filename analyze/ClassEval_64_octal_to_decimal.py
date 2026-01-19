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
    power = 0
    
    # Process digits from right to left
    for i in range(len(octal_num) - 1, -1, -1):
        digit = int(octal_num[i])
        decimal += digit * (8 ** power)
        power += 1
    
    return decimal
@staticmethod
def octal_to_decimal(octal_num):
    """
    Converti un numero dal formato ottale al formato decimale.
    :param octal_num: str, numero ottale
    :return: int, la rappresentazione decimale del numero ottale str.
    >>> NumberConverter.octal_to_decimal('122667')
    42423
    """
    decimal_num = 0
    power = 0
    
    # Iterate through the octal string from right to left
    for i in range(len(octal_num) - 1, -1, -1):
        digit = int(octal_num[i])
        decimal_num += digit * (8 ** power)
        power += 1
    
    return decimal_num
@staticmethod
def decimal_to_octal(decimal_num):
    """
    Convertire un numero dal formato decimale al formato ottale.
    :param decimal_num: int, numero decimale
    :return: str, la rappresentazione ottale di un intero.
    >>> NumberConverter.decimal_to_octal(42423)
    '122667'
    """
    if decimal_num == 0:
        return '0'
    
    octal_str = ''
    num = abs(decimal_num)
    
    while num > 0:
        remainder = num % 8
        octal_str = str(remainder) + octal_str
        num = num // 8
    
    if decimal_num < 0:
        octal_str = '-' + octal_str
    
    return octal_str
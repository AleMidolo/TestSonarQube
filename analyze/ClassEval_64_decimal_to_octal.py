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
    
    octal_digits = []
    num = abs(decimal_num)
    
    while num > 0:
        octal_digits.append(str(num % 8))
        num //= 8
    
    octal_str = ''.join(reversed(octal_digits))
    
    if decimal_num < 0:
        octal_str = '-' + octal_str
    
    return octal_str
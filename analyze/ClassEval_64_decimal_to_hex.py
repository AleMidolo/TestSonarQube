@staticmethod
def decimal_to_hex(decimal_num):
    """
    Convierte un número del formato decimal al formato hexadecimal.
    :param decimal_num: int, número decimal
    :return hex_num: str, la representación hexadecimal de un entero.
    >>> NumberConverter.decimal_to_hex(42423)
    'a5b7'
    """
    if decimal_num == 0:
        return '0'
    
    hex_digits = '0123456789abcdef'
    hex_num = ''
    
    num = abs(decimal_num)
    
    while num > 0:
        remainder = num % 16
        hex_num = hex_digits[remainder] + hex_num
        num = num // 16
    
    if decimal_num < 0:
        hex_num = '-' + hex_num
    
    return hex_num
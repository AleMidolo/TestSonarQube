@staticmethod
def decimal_to_octal(decimal_num):
    """
    将十进制数字转换为八进制格式。
    :param decimal_num: int, 十进制数字
    :return: str, 整数的八进制表示。
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
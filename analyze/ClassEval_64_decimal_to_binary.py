def decimal_to_binary(decimal_num):
    """
    将一个数字从十进制格式转换为二进制格式。
    :param decimal_num: int, 十进制数字
    :return: str, 整数的二进制表示。
    >>> NumberConverter.decimal_to_binary(42423)
    '1010010110110111'
    """
    if decimal_num == 0:
        return '0'
    
    binary_str = ''
    num = abs(decimal_num)
    
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num = num // 2
    
    if decimal_num < 0:
        binary_str = '-' + binary_str
    
    return binary_str
def decimal_to_binary(decimal_num):
    """
    Convert a number from decimal format to binary format.
    :param decimal_num: int, decimal number
    :return: str, the binary representation of an integer.
    >>> NumberConverter.decimal_to_binary(42423)
    '1010010110110111'
    """
    if decimal_num == 0:
        return '0'
    
    binary = ''
    num = abs(decimal_num)
    
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    
    if decimal_num < 0:
        return '-' + binary
    
    return binary
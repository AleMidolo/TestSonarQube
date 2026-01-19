def decimal_to_binary(decimal_num):
    """
    Convertir un número del formato decimal al formato binario.
    :param decimal_num: int, número decimal
    :return: str, la representación binaria de un entero.
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
def decimal_to_binary(decimal_num):
    """
    Converti un numero dal formato decimale al formato binario.
    :param decimal_num: int, numero decimale
    :return: str, la rappresentazione binaria di un intero.
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
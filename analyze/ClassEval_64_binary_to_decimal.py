@staticmethod
def binary_to_decimal(binary_num):
    """
    Convierte un número del formato binario al formato decimal.
    :param binary_num: str, número binario
    :return: int, la representación decimal del número binario str.
    >>> NumberConverter.binary_to_decimal('1010010110110111')
    42423
    """
    decimal = 0
    power = 0
    
    # Iterate through the binary string from right to left
    for i in range(len(binary_num) - 1, -1, -1):
        if binary_num[i] == '1':
            decimal += 2 ** power
        power += 1
    
    return decimal
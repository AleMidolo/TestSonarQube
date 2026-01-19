@staticmethod
def binary_to_decimal(binary_num):
    """
    Convert a number from binary format to decimal format.
    :param binary_num: str, binary number
    :return: int, the decimal representation of binary number str.
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
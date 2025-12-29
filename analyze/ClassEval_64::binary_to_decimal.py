@staticmethod
def binary_to_decimal(binary_num):
    """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """
    decimal_num = int(binary_num, 2)
    return decimal_num
@staticmethod
def binary_to_decimal(binary_num):
    """
        Convierte un número del formato binario al formato decimal.
        :param binary_num: str, número binario
        :return: int, la representación decimal del número binario str.
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """
    decimal_num = int(binary_num, 2)
    return decimal_num
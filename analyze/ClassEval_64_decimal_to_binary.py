@staticmethod
def decimal_to_binary(decimal_num):
    """
        Convertir un número del formato decimal al formato binario.
        :param decimal_num: int, número decimal
        :return: str, la representación binaria de un entero.
        >>> NumberConverter.decimal_to_binary(42423)
        '1010010110110111'
        """
    binary_num = bin(decimal_num)[2:]
    return binary_num
@staticmethod
def decimal_to_binary(decimal_num):
    """
        Converti un numero dal formato decimale al formato binario.
        :param decimal_num: int, numero decimale
        :return: str, la rappresentazione binaria di un intero.
        >>> NumberConverter.decimal_to_binary(42423)
        '1010010110110111'
        """
    binary_num = bin(decimal_num)[2:]
    return binary_num
@staticmethod
def decimal_to_hex(decimal_num):
    """
    Convertire un numero dal formato decimale al formato esadecimale.
    :param decimal_num: int, numero decimale
    :return hex_num: str, la rappresentazione esadecimale di un intero.
    >>> NumberConverter.decimal_to_hex(42423)
    'a5b7'
    """
    return hex(decimal_num)[2:]
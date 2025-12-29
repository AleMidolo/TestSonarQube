@staticmethod
def decimal_to_octal(decimal_num):
    """
        Convertire un numero dal formato decimale al formato ottale.
        :param decimal_num: int, numero decimale
        :return: str, la rappresentazione ottale di un intero.
        >>> NumberConverter.decimal_to_octal(42423)
        '122667'
        """
    octal_num = oct(decimal_num)[2:]
    return octal_num
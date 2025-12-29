@staticmethod
def octal_to_decimal(octal_num):
    """
        Converti un numero dal formato ottale al formato decimale.
        :param octal_num: str, numero ottale
        :return: int, la rappresentazione decimale del numero ottale str.
        >>> NumberConverter.octal_to_decimal('122667')
        42423
        """
    decimal_num = int(octal_num, 8)
    return decimal_num
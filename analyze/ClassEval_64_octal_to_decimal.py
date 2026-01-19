@staticmethod
def octal_to_decimal(octal_num):
    """
    将一个八进制数字转换为十进制格式。
    :param octal_num: str, 八进制数字
    :return: int, 八进制数字的十进制表示。
    >>> NumberConverter.octal_to_decimal('122667')
    42423
    """
    return int(octal_num, 8)
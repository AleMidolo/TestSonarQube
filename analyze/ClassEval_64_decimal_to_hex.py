@staticmethod
def decimal_to_hex(decimal_num):
    """
    将一个数字从十进制格式转换为十六进制格式。
    :param decimal_num: int, 十进制数字
    :return hex_num: str, 整数的十六进制表示。
    >>> NumberConverter.decimal_to_hex(42423)
    'a5b7'
    """
    return hex(decimal_num)[2:]
@staticmethod
def hex_to_decimal(hex_num):
    """
        将一个数字从十六进制格式转换为十进制格式。
        :param hex_num: str, 十六进制数字
        :return: int, 十六进制数字字符串的十进制表示。
        >>> NumberConverter.hex_to_decimal('a5b7')
        42423
        """
    decimal_num = int(hex_num, 16)
    return decimal_num
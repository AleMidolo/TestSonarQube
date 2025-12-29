@staticmethod
def decimal_to_octal(decimal_num):
    """
        将十进制数字转换为八进制格式。
        :param decimal_num: int, 十进制数字
        :return: str, 整数的八进制表示。
        >>> NumberConverter.decimal_to_octal(42423)
        '122667'
        """
    octal_num = oct(decimal_num)[2:]
    return octal_num
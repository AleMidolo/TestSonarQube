@staticmethod
def decimal_to_binary(decimal_num):
    """
        将一个数字从十进制格式转换为二进制格式。
        :param decimal_num: int, 十进制数字
        :return: str, 整数的二进制表示。
        >>> NumberConverter.decimal_to_binary(42423)
        '1010010110110111'
        """
    binary_num = bin(decimal_num)[2:]
    return binary_num
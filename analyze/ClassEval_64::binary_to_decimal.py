@staticmethod
def binary_to_decimal(binary_num):
    """
        将一个数字从二进制格式转换为十进制格式。
        :param binary_num: str, 二进制数字
        :return: int, 二进制数字的十进制表示。
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """
    decimal_num = int(binary_num, 2)
    return decimal_num
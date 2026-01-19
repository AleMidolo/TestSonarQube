@staticmethod
def octal_to_decimal(octal_num):
    """
    将一个八进制数字转换为十进制格式。
    :param octal_num: str, 八进制数字
    :return: int, 八进制数字的十进制表示。
    >>> NumberConverter.octal_to_decimal('122667')
    42423
    """
    decimal_num = 0
    power = 0
    
    # Iterate through the octal string from right to left
    for i in range(len(octal_num) - 1, -1, -1):
        digit = int(octal_num[i])
        decimal_num += digit * (8 ** power)
        power += 1
    
    return decimal_num
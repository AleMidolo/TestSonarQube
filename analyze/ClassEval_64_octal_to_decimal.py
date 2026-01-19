@staticmethod
def octal_to_decimal(octal_num):
    """
    एक संख्या को ऑक्टल प्रारूप से दशमलव प्रारूप में परिवर्तित करें।
    :param octal_num: str, ऑक्टल संख्या
    :return: int, ऑक्टल संख्या का दशमलव प्रतिनिधित्व।
    >>> NumberConverter.octal_to_decimal('122667')
    42423
    """
    decimal_num = 0
    power = 0
    
    # Iterate through the octal number from right to left
    for i in range(len(octal_num) - 1, -1, -1):
        digit = int(octal_num[i])
        decimal_num += digit * (8 ** power)
        power += 1
    
    return decimal_num
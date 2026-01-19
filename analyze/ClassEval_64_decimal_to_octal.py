@staticmethod
def decimal_to_octal(decimal_num):
    """
    एक संख्या को दशमलव प्रारूप से ऑक्टल प्रारूप में परिवर्तित करें।
    :param decimal_num: int, दशमलव संख्या
    :return: str, एक पूर्णांक का ऑक्टल प्रतिनिधित्व।
    >>> NumberConverter.decimal_to_octal(42423)
    '122667'
    """
    if decimal_num == 0:
        return '0'
    
    octal_digits = []
    num = abs(decimal_num)
    
    while num > 0:
        remainder = num % 8
        octal_digits.append(str(remainder))
        num = num // 8
    
    octal_result = ''.join(reversed(octal_digits))
    
    if decimal_num < 0:
        octal_result = '-' + octal_result
    
    return octal_result
@staticmethod
def hex_to_decimal(hex_num):
    """
    एक संख्या को हेक्स प्रारूप से दशमलव प्रारूप में परिवर्तित करें।
    :param hex_num: str, हेक्स संख्या
    :return: int, हेक्स संख्या के दशमलव प्रतिनिधित्व।
    >>> NumberConverter.hex_to_decimal('a5b7')
    42423
    """
    return int(hex_num, 16)
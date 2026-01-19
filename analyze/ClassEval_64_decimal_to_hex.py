@staticmethod
def decimal_to_hex(decimal_num):
    """
    दशमलव प्रारूप से हेक्स प्रारूप में एक संख्या को परिवर्तित करें।
    :param decimal_num: int, दशमलव संख्या
    :return hex_num: str, एक पूर्णांक का हेक्स प्रतिनिधित्व।
    >>> NumberConverter.decimal_to_hex(42423)
    'a5b7'
    """
    return hex(decimal_num)[2:]
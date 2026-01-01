@staticmethod
def decimal_to_octal(decimal_num):
    """
        एक संख्या को दशमलव प्रारूप से ऑक्टल प्रारूप में परिवर्तित करें।
        :param decimal_num: int, दशमलव संख्या
        :return: str, एक पूर्णांक का ऑक्टल प्रतिनिधित्व।
        >>> NumberConverter.decimal_to_octal(42423)
        '122667'
        """
    octal_num = oct(decimal_num)[2:]
    return octal_num
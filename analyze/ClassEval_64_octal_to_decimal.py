@staticmethod
def octal_to_decimal(octal_num):
    """
        एक संख्या को ऑक्टल प्रारूप से दशमलव प्रारूप में परिवर्तित करें।
        :param octal_num: str, ऑक्टल संख्या
        :return: int, ऑक्टल संख्या का दशमलव प्रतिनिधित्व।
        >>> NumberConverter.octal_to_decimal('122667')
        42423
        """
    decimal_num = int(octal_num, 8)
    return decimal_num
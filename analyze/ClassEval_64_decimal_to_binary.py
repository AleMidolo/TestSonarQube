@staticmethod
def decimal_to_binary(decimal_num):
    """
        एक संख्या को दशमलव प्रारूप से बाइनरी प्रारूप में परिवर्तित करें।
        :param decimal_num: int, दशमलव संख्या
        :return: str, एक पूर्णांक का बाइनरी प्रतिनिधित्व।
        >>> NumberConverter.decimal_to_binary(42423)
        '1010010110110111'
        """
    binary_num = bin(decimal_num)[2:]
    return binary_num
@staticmethod
def binary_to_decimal(binary_num):
    """
    बाइनरी प्रारूप से दशमलव प्रारूप में एक संख्या को परिवर्तित करें।
    :param binary_num: str, बाइनरी संख्या
    :return: int, बाइनरी संख्या str का दशमलव प्रतिनिधित्व।
    >>> NumberConverter.binary_to_decimal('1010010110110111')
    42423
    """
    return int(binary_num, 2)
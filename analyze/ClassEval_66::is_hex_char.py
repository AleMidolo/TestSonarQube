@staticmethod
def is_hex_char(char):
    """
        确定给定字符是否为十六进制数字。
        :param char: str，要检查的字符。
        :return: bool，如果字符是十六进制数字则为 True，否则为 False。
        >>> NumericEntityUnescaper.is_hex_char('a')
        True
        """
    return char in '0123456789abcdefABCDEF'
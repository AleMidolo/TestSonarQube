@staticmethod
def is_hex_char(char):
    """
        यह निर्धारित करता है कि दिया गया चर एक हेक्साडेसिमल अंक है या नहीं।
        :param char: str, जांचने के लिए चर।
        :return: bool, यदि चर एक हेक्साडेसिमल अंक है तो True, अन्यथा False।
        >>> NumericEntityUnescaper.is_hex_char('a')
        True
        """
    return char in '0123456789abcdefABCDEF'
@staticmethod
def is_hex_char(char):
    """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True
        """
    return char.isdigit() or (char.lower() >= 'a' and char.lower() <= 'f')
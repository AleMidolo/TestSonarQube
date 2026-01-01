@staticmethod
def is_hex_char(char):
    """
        Determina si un carácter dado es un dígito hexadecimal.
        :param char: str, el carácter a verificar.
        :return: bool, True si el carácter es un dígito hexadecimal, False en caso contrario.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True

        """
    return '0' <= char <= '9' or 'a' <= char <= 'f' or 'A' <= char <= 'F'
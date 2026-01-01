@staticmethod
def is_hex_char(char):
    """
        Determina se un dato carattere è una cifra esadecimale.
        :param char: str, il carattere da controllare.
        :return: bool, True se il carattere è una cifra esadecimale, False altrimenti.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True
        """
    return '0' <= char <= '9' or 'a' <= char <= 'f' or 'A' <= char <= 'F'
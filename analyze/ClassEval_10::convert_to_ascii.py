def convert_to_ascii(self):
    """
        Convierte la cadena binaria a una cadena ascii.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_ascii()
        'hello'
        """
    return self.convert_to_utf8()
def clean_non_binary_chars(self):
    """
        Limpia la cadena binaria eliminando todos los caracteres que no sean 0 o 1.
        >>> bdp = BinaryDataProcessor("01101000daf3e4r01100101011011000110110001101111")
        >>> bdp.clean_non_binary_chars()
        >>> bdp.binary_string
        '0110100001100101011011000110110001101111'
        """
    self.binary_string = ''.join(filter(lambda x: x in '01', self.binary_string))
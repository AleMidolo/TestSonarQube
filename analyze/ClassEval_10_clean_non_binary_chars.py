def clean_non_binary_chars(self):
    """
    Clean the binary string by removing all non 0 or 1 characters.
    >>> bdp = BinaryDataProcessor("01101000daf3e4r01100101011011000110110001101111")
    >>> bdp.clean_non_binary_chars()
    >>> bdp.binary_string
    '0110100001100101011011000110110001101111'

    """
    self.binary_string = ''.join(char for char in self.binary_string if char in '01')
def clean_non_binary_chars(self):
    """
        बाइनरी स्ट्रिंग को साफ करें सभी गैर 0 या 1 वर्णों को हटाकर।
        >>> bdp = BinaryDataProcessor("01101000daf3e4r01100101011011000110110001101111")
        >>> bdp.clean_non_binary_chars()
        >>> bdp.binary_string
        '0110100001100101011011000110110001101111'
        """
    self.binary_string = ''.join(filter(lambda x: x in '01', self.binary_string))
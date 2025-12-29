def clean_non_binary_chars(self):
    """
        通过移除所有非 0 或 1 的字符来清理二进制字符串。
        >>> bdp = BinaryDataProcessor("01101000daf3e4r01100101011011000110110001101111")
        >>> bdp.clean_non_binary_chars()
        >>> bdp.binary_string
        '0110100001100101011011000110110001101111'
        """
    self.binary_string = ''.join(filter(lambda x: x in '01', self.binary_string))
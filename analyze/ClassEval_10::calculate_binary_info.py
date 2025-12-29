def calculate_binary_info(self):
    """
        计算二进制字符串的信息，包括0和1的百分比，以及二进制字符串的总长度。
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

        """
    if not self.binary_string:
        return {'Zeroes': 0.0, 'Ones': 0.0, 'Bit length': 0}
    total_length = len(self.binary_string)
    zero_count = self.binary_string.count('0')
    one_count = self.binary_string.count('1')
    zero_percentage = zero_count / total_length
    one_percentage = one_count / total_length
    return {'Zeroes': round(zero_percentage, 3), 'Ones': round(one_percentage, 3), 'Bit length': total_length}
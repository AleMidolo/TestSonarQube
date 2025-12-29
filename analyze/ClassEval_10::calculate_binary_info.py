def calculate_binary_info(self):
    """
        计算二进制字符串的信息，包括0和1的百分比，以及二进制字符串的总长度。
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}
        """
    total_length = len(self.binary_string)
    if total_length == 0:
        return {'Zeroes': 0, 'Ones': 0, 'Bit length': 0}
    count_zeroes = self.binary_string.count('0')
    count_ones = self.binary_string.count('1')
    return {'Zeroes': count_zeroes / total_length, 'Ones': count_ones / total_length, 'Bit length': total_length}
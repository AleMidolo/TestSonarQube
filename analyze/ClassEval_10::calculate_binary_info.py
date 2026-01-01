def calculate_binary_info(self):
    """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}
        """
    total_length = len(self.binary_string)
    if total_length == 0:
        return {'Zeroes': 0, 'Ones': 0, 'Bit length': 0}
    count_ones = self.binary_string.count('1')
    count_zeroes = total_length - count_ones
    return {'Zeroes': round(count_zeroes / total_length, 3), 'Ones': round(count_ones / total_length, 3), 'Bit length': total_length}
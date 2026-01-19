def calculate_binary_info(self):
    """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}
        """
    if not self.binary_string:
        return {'Zeroes': 0.0, 'Ones': 0.0, 'Bit length': 0}
    total_bits = len(self.binary_string)
    zeros_count = self.binary_string.count('0')
    ones_count = self.binary_string.count('1')
    return {'Zeroes': round(zeros_count / total_bits, 3), 'Ones': round(ones_count / total_bits, 3), 'Bit length': total_bits}
def calculate_binary_info(self):
    """
        बाइनरी स्ट्रिंग की जानकारी की गणना करें, जिसमें 0 और 1 का प्रतिशत, और बाइनरी स्ट्रिंग की कुल लंबाई शामिल है।
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101110")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

        """
    if not self.binary_string:
        return {'Zeroes': 0.0, 'Ones': 0.0, 'Bit length': 0}
    total_bits = len(self.binary_string)
    zero_count = self.binary_string.count('0')
    one_count = self.binary_string.count('1')
    zero_percentage = zero_count / total_bits
    one_percentage = one_count / total_bits
    return {'Zeroes': round(zero_percentage, 3), 'Ones': round(one_percentage, 3), 'Bit length': total_bits}
def calculate_binary_info(self):
    """
        बाइनरी स्ट्रिंग की जानकारी की गणना करें, जिसमें 0 और 1 का प्रतिशत, और बाइनरी स्ट्रिंग की कुल लंबाई शामिल है।
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101110")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}
        """
    total_bits = len(self.binary_string)
    if total_bits == 0:
        return {'Zeroes': 0, 'Ones': 0, 'Bit length': 0}
    count_zeroes = self.binary_string.count('0')
    count_ones = total_bits - count_zeroes
    return {'Zeroes': count_zeroes / total_bits, 'Ones': count_ones / total_bits, 'Bit length': total_bits}
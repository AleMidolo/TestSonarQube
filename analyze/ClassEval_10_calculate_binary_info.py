def calculate_binary_info(self):
    """
    बाइनरी स्ट्रिंग की जानकारी की गणना करें, जिसमें 0 और 1 का प्रतिशत, और बाइनरी स्ट्रिंग की कुल लंबाई शामिल है।
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101110")
    >>> bdp.calculate_binary_info()
    {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

    """
    if not hasattr(self, 'binary_string') or not self.binary_string:
        return {'Zeroes': 0.0, 'Ones': 0.0, 'Bit length': 0}
    
    total_length = len(self.binary_string)
    count_zeros = self.binary_string.count('0')
    count_ones = self.binary_string.count('1')
    
    percentage_zeros = count_zeros / total_length if total_length > 0 else 0.0
    percentage_ones = count_ones / total_length if total_length > 0 else 0.0
    
    return {
        'Zeroes': percentage_zeros,
        'Ones': percentage_ones,
        'Bit length': total_length
    }
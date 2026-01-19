def calculate_binary_info(self):
    """
    计算二进制字符串的信息,包括0和1的百分比,以及二进制字符串的总长度。
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.calculate_binary_info()
    {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

    """
    binary_str = self.binary_data if hasattr(self, 'binary_data') else self.data
    
    total_length = len(binary_str)
    
    if total_length == 0:
        return {'Zeroes': 0.0, 'Ones': 0.0, 'Bit length': 0}
    
    count_zeros = binary_str.count('0')
    count_ones = binary_str.count('1')
    
    percent_zeros = count_zeros / total_length
    percent_ones = count_ones / total_length
    
    return {
        'Zeroes': percent_zeros,
        'Ones': percent_ones,
        'Bit length': total_length
    }
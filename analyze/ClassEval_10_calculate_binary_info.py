def calculate_binary_info(self):
    """
    Calcola le informazioni sulla stringa binaria, inclusa la percentuale di 0 e 1, e la lunghezza totale della stringa binaria.
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.calculate_binary_info()
    {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

    """
    binary_string = self.binary_string
    total_length = len(binary_string)
    
    if total_length == 0:
        return {'Zeroes': 0.0, 'Ones': 0.0, 'Bit length': 0}
    
    count_zeroes = binary_string.count('0')
    count_ones = binary_string.count('1')
    
    percentage_zeroes = count_zeroes / total_length
    percentage_ones = count_ones / total_length
    
    return {
        'Zeroes': percentage_zeroes,
        'Ones': percentage_ones,
        'Bit length': total_length
    }
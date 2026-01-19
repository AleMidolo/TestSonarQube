def calculate_binary_info(self):
    """
        Calcola le informazioni sulla stringa binaria, inclusa la percentuale di 0 e 1, e la lunghezza totale della stringa binaria.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}
        """
    total_bits = len(self.binary_string)
    if total_bits == 0:
        return {'Zeroes': 0, 'Ones': 0, 'Bit length': 0}
    count_zeroes = self.binary_string.count('0')
    count_ones = self.binary_string.count('1')
    return {'Zeroes': count_zeroes / total_bits, 'Ones': count_ones / total_bits, 'Bit length': total_bits}
def calculate_binary_info(self):
    """
        Calcular la información de la cadena binaria, incluyendo el porcentaje de 0 y 1, y la longitud total de la cadena binaria.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Ceros': 0.475, 'Unos': 0.525, 'Longitud de bits': 40}

        """
    if not self.binary_string:
        return {'Ceros': 0.0, 'Unos': 0.0, 'Longitud de bits': 0}
    total_bits = len(self.binary_string)
    count_zeros = self.binary_string.count('0')
    count_ones = self.binary_string.count('1')
    return {'Ceros': round(count_zeros / total_bits, 3), 'Unos': round(count_ones / total_bits, 3), 'Longitud de bits': total_bits}
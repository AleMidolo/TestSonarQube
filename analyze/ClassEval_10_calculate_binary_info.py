def calculate_binary_info(self):
    """
    Calcular la información de la cadena binaria, incluyendo el porcentaje de 0 y 1, y la longitud total de la cadena binaria.
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.calculate_binary_info()
    {'Ceros': 0.475, 'Unos': 0.525, 'Longitud de bits': 40}

    """
    # Assuming self has a binary string attribute (e.g., self.binary_string)
    binary_str = self.binary_string
    
    # Calculate the total length
    total_length = len(binary_str)
    
    # Count zeros and ones
    count_zeros = binary_str.count('0')
    count_ones = binary_str.count('1')
    
    # Calculate percentages
    percentage_zeros = count_zeros / total_length if total_length > 0 else 0
    percentage_ones = count_ones / total_length if total_length > 0 else 0
    
    return {
        'Ceros': percentage_zeros,
        'Unos': percentage_ones,
        'Longitud de bits': total_length
    }
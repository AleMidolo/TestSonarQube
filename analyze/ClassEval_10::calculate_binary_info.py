def calculate_binary_info(self):
        """
        बाइनरी स्ट्रिंग की जानकारी की गणना करें, जिसमें 0 और 1 का प्रतिशत, और बाइनरी स्ट्रिंग की कुल लंबाई शामिल है।
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101110")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

        """
        total_length = len(self.binary_string)
        if total_length == 0:
            return {'Zeroes': 0.0, 'Ones': 0.0, 'Bit length': 0}

        count_zeroes = self.binary_string.count('0')
        count_ones = self.binary_string.count('1')

        return {
            'Zeroes': count_zeroes / total_length,
            'Ones': count_ones / total_length,
            'Bit length': total_length
        }
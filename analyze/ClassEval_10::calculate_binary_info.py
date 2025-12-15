def calculate_binary_info(self):
        """
        बाइनरी स्ट्रिंग की जानकारी की गणना करें, जिसमें 0 और 1 का प्रतिशत, और बाइनरी स्ट्रिंग की कुल लंबाई शामिल है।
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101110")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

        """
        total_length = len(self.binary_string)
        zeroes = self.binary_string.count('0')
        ones = self.binary_string.count('1')
        
        return {
            'Zeroes': zeroes / total_length,
            'Ones': ones / total_length,
            'Bit length': total_length
        }
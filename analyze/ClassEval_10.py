class BinaryDataProcessor:
    def __init__(self, binary_string):
        self.binary_string = self.clean_non_binary_chars(binary_string)

    def clean_non_binary_chars(self, binary_string):
        return ''.join(filter(lambda x: x in '01', binary_string))

    def calculate_binary_info(self):
        total_length = len(self.binary_string)
        zeroes_count = self.binary_string.count('0')
        ones_count = self.binary_string.count('1')

        return {
            'Zeroes': self.calculate_percentage(zeroes_count, total_length),
            'Ones': self.calculate_percentage(ones_count, total_length),
            'Bit length': total_length
        }

    def calculate_percentage(self, count, total):
        return count / total if total > 0 else 0

    def convert_to_ascii(self):
        return self.convert_to_encoding('ascii')

    def convert_to_utf8(self):
        return self.convert_to_encoding('utf-8')

    def convert_to_encoding(self, encoding):
        byte_array = bytearray()
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i+8]
            decimal = int(byte, 2)
            byte_array.append(decimal)

        return byte_array.decode(encoding)
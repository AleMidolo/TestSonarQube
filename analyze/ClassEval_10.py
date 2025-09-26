class BinaryDataProcessor:
    def __init__(self, binary_string):
        self.binary_string = self.clean_non_binary_chars(binary_string)

    def clean_non_binary_chars(self, binary_string):
        return ''.join(filter(lambda x: x in '01', binary_string))

    def calculate_binary_info(self):
        total_length = len(self.binary_string)
        zeroes_count = self.count_bits('0')
        ones_count = self.count_bits('1')

        zeroes_percentage = self.calculate_percentage(zeroes_count, total_length)
        ones_percentage = self.calculate_percentage(ones_count, total_length)

        return {
            'Zeroes': zeroes_percentage,
            'Ones': ones_percentage,
            'Bit length': total_length
        }

    def count_bits(self, bit):
        return self.binary_string.count(bit)

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
def convert_to_utf8(self):
    """
        Convert the binary string to utf-8 string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_utf8()
        'hello'

        """
    byte_array = bytearray()
    for i in range(0, len(self.binary_string), 8):
        byte = self.binary_string[i:i + 8]
        decimal = int(byte, 2)
        byte_array.append(decimal)
    return byte_array.decode('utf-8')
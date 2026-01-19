def convert_to_ascii(self):
    """
        将二进制字符串转换为 ASCII 字符串。
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_ascii()
        'hello'

        """
    byte_array = bytearray()
    for i in range(0, len(self.binary_string), 8):
        byte = self.binary_string[i:i + 8]
        if len(byte) == 8:
            decimal = int(byte, 2)
            byte_array.append(decimal)
    return byte_array.decode('ascii')
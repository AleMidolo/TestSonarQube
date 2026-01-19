def convert_to_utf8(self):
    """
    Convert the binary string to utf-8 string.
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.convert_to_utf8()
    'hello'

    """
    # Split binary string into 8-bit chunks
    binary_str = self.binary_string
    bytes_list = []
    
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        # Convert each 8-bit chunk to integer, then to character
        bytes_list.append(int(byte, 2))
    
    # Convert list of byte values to bytes object, then decode to UTF-8
    return bytes(bytes_list).decode('utf-8')
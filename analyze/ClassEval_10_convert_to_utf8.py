def convert_to_utf8(self):
    """
    Convierte la cadena binaria a una cadena utf-8.
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.convert_to_utf8()
    'hello'

    """
    # Split the binary string into chunks of 8 bits (1 byte each)
    binary_str = self.data if hasattr(self, 'data') else self
    bytes_list = []
    
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        # Convert each 8-bit chunk to an integer, then to a character
        bytes_list.append(int(byte, 2))
    
    # Convert the list of byte values to a UTF-8 string
    return bytes(bytes_list).decode('utf-8')
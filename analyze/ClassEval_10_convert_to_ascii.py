def convert_to_ascii(self):
    """
    Convierte la cadena binaria a una cadena ascii.
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.convert_to_ascii()
    'hello'

    """
    result = ""
    # Process the binary string in chunks of 8 bits
    for i in range(0, len(self.binary_string), 8):
        # Extract 8-bit chunk
        byte = self.binary_string[i:i+8]
        # Convert binary to decimal and then to ASCII character
        if len(byte) == 8:
            result += chr(int(byte, 2))
    return result
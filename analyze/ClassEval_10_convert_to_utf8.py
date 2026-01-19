def convert_to_utf8(self):
    """
    Convert the binary string to utf-8 string.
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.convert_to_utf8()
    'hello'

    """
    # Split binary string into 8-bit chunks
    binary_str = self.binary_string
    chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    
    # Convert each 8-bit chunk to its corresponding character
    result = ''.join(chr(int(chunk, 2)) for chunk in chunks)
    
    return result
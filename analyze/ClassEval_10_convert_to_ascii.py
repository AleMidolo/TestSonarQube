def convert_to_ascii(self):
    """
    बाइनरी स्ट्रिंग को एएससीआईआई स्ट्रिंग में परिवर्तित करें।
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.convert_to_ascii()
    'hello'

    """
    binary_string = self.data if hasattr(self, 'data') else self
    result = ""
    
    # Process binary string in chunks of 8 bits
    for i in range(0, len(binary_string), 8):
        # Extract 8-bit chunk
        byte = binary_string[i:i+8]
        # Convert binary to decimal and then to ASCII character
        if len(byte) == 8:
            ascii_char = chr(int(byte, 2))
            result += ascii_char
    
    return result
def convert_to_utf8(self):
    """
    बाइनरी स्ट्रिंग को utf-8 स्ट्रिंग में परिवर्तित करें।
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.convert_to_utf8()
    'hello'

    """
    binary_string = self.data if hasattr(self, 'data') else self
    
    # Split binary string into 8-bit chunks
    byte_chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    
    # Convert each 8-bit chunk to its corresponding character
    result = ''
    for chunk in byte_chunks:
        if len(chunk) == 8:  # Ensure we have a complete byte
            decimal_value = int(chunk, 2)
            result += chr(decimal_value)
    
    return result
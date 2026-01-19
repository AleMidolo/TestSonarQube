def convert_to_utf8(self):
    """
    将二进制字符串转换为utf-8字符串。
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.convert_to_utf8()
    'hello'

    """
    binary_str = self.data
    # Split binary string into 8-bit chunks
    bytes_list = []
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) == 8:
            bytes_list.append(int(byte, 2))
    
    # Convert bytes to UTF-8 string
    return bytes(bytes_list).decode('utf-8')
def convert_to_ascii(self):
    """
    将二进制字符串转换为 ASCII 字符串。
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.convert_to_ascii()
    'hello'

    """
    binary_str = self.data
    ascii_str = ""
    
    # 将二进制字符串按8位分组
    for i in range(0, len(binary_str), 8):
        # 获取8位二进制
        byte = binary_str[i:i+8]
        # 转换为十进制再转换为ASCII字符
        ascii_str += chr(int(byte, 2))
    
    return ascii_str
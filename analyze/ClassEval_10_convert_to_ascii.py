def convert_to_ascii(self):
    """
    将二进制字符串转换为 ASCII 字符串。
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.convert_to_ascii()
    'hello'

    """
    result = []
    # 将二进制字符串按每8位分组
    for i in range(0, len(self.data), 8):
        # 提取8位二进制
        byte = self.data[i:i+8]
        # 将二进制转换为整数，再转换为ASCII字符
        if len(byte) == 8:  # 确保是完整的8位
            result.append(chr(int(byte, 2)))
    
    return ''.join(result)
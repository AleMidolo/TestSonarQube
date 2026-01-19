def convert_to_utf8(self):
    """
    将二进制字符串转换为utf-8字符串。
    >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
    >>> bdp.convert_to_utf8()
    'hello'

    """
    binary_str = self.data
    # 将二进制字符串按8位分组
    bytes_list = []
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        # 将每8位二进制转换为整数，再转换为字节
        bytes_list.append(int(byte, 2))
    
    # 将字节列表转换为bytes对象，然后解码为utf-8字符串
    return bytes(bytes_list).decode('utf-8')
def get_binary(self):
    """
        如果IP地址有效，返回IP地址的二进制形式；否则，返回''
        :return: 字符串
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
    if not self.is_valid():
        return ''
    octets = self.get_octets()
    binary_octets = []
    for octet in octets:
        binary = bin(int(octet))[2:]
        binary_octets.append(binary.zfill(8))
    return '.'.join(binary_octets)
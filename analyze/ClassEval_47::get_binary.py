def get_binary(self):
    """
        如果IP地址有效，返回IP地址的二进制形式；否则，返回''
        :return: 字符串
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
    if self.is_valid():
        return '.'.join((format(int(octet), '08b') for octet in self.ip_address.split('.')))
    else:
        return ''
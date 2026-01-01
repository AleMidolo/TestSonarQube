def get_octets(self):
    """
        如果IP地址有效，则返回由“.”分隔的四个十进制数字组成的列表；否则，返回一个空列表
        :return: list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ["10", "10", "10", "10"]
        """
    if self.is_valid():
        return self.ip_address.split('.')
    else:
        return []
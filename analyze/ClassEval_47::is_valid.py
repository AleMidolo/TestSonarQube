def is_valid(self):
    """
        判断IP地址是否有效，即IP地址是否由四个十进制数字组成，并且用'.'分隔。每个数字大于等于0且小于等于255。
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        """
    octets = self.ip_address.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit() or not 0 <= int(octet) <= 255:
            return False
    return True
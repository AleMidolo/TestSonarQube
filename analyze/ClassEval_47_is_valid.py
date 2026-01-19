def is_valid(self):
    """
        判断IP地址是否有效，即IP地址是否由四个十进制数字组成，并且用'.'分隔。每个数字大于等于0且小于等于255。
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        """
    parts = self.ip_address.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
        if len(part) > 1 and part[0] == '0':
            return False
    return True
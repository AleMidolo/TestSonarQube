@staticmethod
def is_valid_ipv6(ip_address):
    """
        检查给定的 IP 地址是否是有效的 IPv6 地址。
        :param ip_address:字符串, 要检查的 IP 地址
        :return:布尔值, 如果 IP 地址有效则返回 True，否则返回 False
        >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
        True
        >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334')
        False

        """
    try:
        socket.inet_pton(socket.AF_INET6, ip_address)
        return True
    except socket.error:
        return False
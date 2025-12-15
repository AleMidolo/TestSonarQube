def is_valid_ipv4(ip_address):
        """
        检查给定的 IP 地址是否是有效的 IPv4 地址。
        :param ip_address: 字符串，要检查的 IP 地址
        :return: 布尔值，如果 IP 地址有效则返回 True，否则返回 False
        >>> IpUtil.is_valid_ipv4('192.168.0.123')
        True
        >>> IpUtil.is_valid_ipv4('256.0.0.0')
        False

        """
        import socket

        try:
            socket.inet_pton(socket.AF_INET, ip_address)
            return True
        except socket.error:
            return False
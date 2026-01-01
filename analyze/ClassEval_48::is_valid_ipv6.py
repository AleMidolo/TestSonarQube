@staticmethod
def is_valid_ipv6(ip_address):
    """
        Check if the given IP address is a valid IPv6 address.
        :param ip_address:string, the IP address to check
        :return:bool, True if the IP address is valid, False otherwise
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
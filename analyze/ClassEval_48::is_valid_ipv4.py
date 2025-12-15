def is_valid_ipv4(ip_address):
    """
    Check if the given IP address is a valid IPv4 address.
    :param ip_address: string, the IP address to check
    :return: bool, True if the IP address is valid, False otherwise
    >>> IpUtil.is_valid_ipv4('192.168.0.123')
    True
    >>> IpUtil.is_valid_ipv4('256.0.0.0')
    False

    """
    try:
        socket.inet_pton(socket.AF_INET, ip_address)
        return True
    except socket.error:
        return False
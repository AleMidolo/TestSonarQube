@staticmethod
def get_hostname(ip_address):
    """
        Get the hostname associated with the given IP address.
        :param ip_address:string, the IP address to get the hostname for
        :return: string, the hostname associated with the IP address
        >>> IpUtil.get_hostname('110.242.68.3')
        'www.baidu.com'
        >>> IpUtil.get_hostname('10.0.0.1')

        """
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        return None
    except socket.gaierror:
        return None
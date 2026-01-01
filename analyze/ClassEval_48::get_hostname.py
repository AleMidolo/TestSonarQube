@staticmethod
def get_hostname(ip_address):
    """
        Obtiene el nombre de host asociado con la dirección IP dada.
        :param ip_address: string, la dirección IP para la cual obtener el nombre de host
        :return: string, el nombre de host asociado con la dirección IP
        >>> IpUtil.get_hostname('110.242.68.3')
        'www.baidu.com'
        >>> IpUtil.get_hostname('10.0.0.1')

        """
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except (socket.herror, socket.gaierror, ValueError):
        return None
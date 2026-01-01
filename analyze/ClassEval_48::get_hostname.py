@staticmethod
def get_hostname(ip_address):
    """
        Ottieni il nome host associato all'indirizzo IP fornito.
        :param ip_address:string, l'indirizzo IP per cui ottenere il nome host
        :return: string, il nome host associato all'indirizzo IP
        >>> IpUtil.get_hostname('110.242.68.3')
        'www.baidu.com'
        >>> IpUtil.get_hostname('10.0.0.1')

        """
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except (socket.herror, socket.gaierror):
        return None
@staticmethod
def get_hostname(ip_address):
    """
        दिए गए IP पते से संबंधित होस्टनाम प्राप्त करें।
        :param ip_address:string, होस्टनाम प्राप्त करने के लिए IP पता
        :return: string, IP पते से संबंधित होस्टनाम
        >>> IpUtil.get_hostname('110.242.68.3')
        'www.baidu.com'
        >>> IpUtil.get_hostname('10.0.0.1')
        """
    try:
        return socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        return None
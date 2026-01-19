@staticmethod
def is_valid_ipv6(ip_address):
    """
        Verifica si la dirección IP dada es una dirección IPv6 válida.
        :param ip_address:string, la dirección IP a verificar
        :return:bool, True si la dirección IP es válida, False en caso contrario
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
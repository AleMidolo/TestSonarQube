@staticmethod
def is_valid_ipv6(ip_address):
    """
    Controlla se l'indirizzo IP fornito è un indirizzo IPv6 valido.
    :param ip_address:string, l'indirizzo IP da controllare
    :return:bool, True se l'indirizzo IP è valido, False altrimenti
    >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
    True
    >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334')
    False

    """
    import socket
    
    try:
        socket.inet_pton(socket.AF_INET6, ip_address)
        return True
    except (socket.error, OSError, AttributeError, TypeError):
        return False
def is_valid_ipv4(ip_address):
    """
    Controlla se l'indirizzo IP fornito è un indirizzo IPv4 valido.
    :param ip_address: stringa, l'indirizzo IP da controllare
    :return: bool, True se l'indirizzo IP è valido, False altrimenti
    >>> is_valid_ipv4('192.168.0.123')
    True
    >>> is_valid_ipv4('256.0.0.0')
    False

    """
    import socket

    try:
        socket.inet_pton(socket.AF_INET, ip_address)
        return True
    except socket.error:
        return False
@staticmethod
def is_valid_ipv4(ip_address):
    """
        Controlla se l'indirizzo IP fornito è un indirizzo IPv4 valido.
        :param ip_address: stringa, l'indirizzo IP da controllare
        :return: bool, True se l'indirizzo IP è valido, False altrimenti
        >>> IpUtil.is_valid_ipv4('192.168.0.123')
        True
        >>> IpUtil.is_valid_ipv4('256.0.0.0')
        False
        """
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True
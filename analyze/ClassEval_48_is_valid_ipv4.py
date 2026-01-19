@staticmethod
def is_valid_ipv4(ip_address):
    """
        Verifica si la dirección IP dada es una dirección IPv4 válida.
        :param ip_address: cadena, la dirección IP a verificar
        :return: bool, True si la dirección IP es válida, False en caso contrario
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
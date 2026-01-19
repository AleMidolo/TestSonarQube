def is_valid(self):
    """
        Juzgar si la dirección IP es válida, es decir, si la dirección IP está compuesta por cuatro dígitos decimales separados por '.'. Cada dígito es mayor o igual a 0 y menor o igual a 255.
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        """
    octets = self.ip_address.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit() or not 0 <= int(octet) <= 255:
            return False
    return True
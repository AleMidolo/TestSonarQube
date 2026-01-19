def is_valid(self):
    """
        Juzgar si la dirección IP es válida, es decir, si la dirección IP está compuesta por cuatro dígitos decimales separados por '.'. Cada dígito es mayor o igual a 0 y menor o igual a 255.
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        """
    parts = self.ip_address.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
        if len(part) > 1 and part[0] == '0':
            return False
    return True
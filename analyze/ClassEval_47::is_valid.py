def is_valid(self):
    """
        Giudica se l'indirizzo IP è valido, cioè se l'indirizzo IP è composto da quattro cifre decimali separate da '.'. Ogni cifra è maggiore o uguale a 0 e minore o uguale a 255.
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
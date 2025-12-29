def is_valid(self):
    """
        Giudica se l'indirizzo IP è valido, cioè se l'indirizzo IP è composto da quattro cifre decimali separate da '.'. Ogni cifra è maggiore o uguale a 0 e minore o uguale a 255.
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        """
    octets = self.get_octets()
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit() or not 0 <= int(octet) <= 255:
            return False
    return True
def get_binary(self):
    """
        Se l'indirizzo IP è valido, restituisce la forma binaria dell'indirizzo IP; altrimenti, restituisce ''
        :return: stringa
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
    if self.is_valid():
        return '.'.join((format(int(octet), '08b') for octet in self.get_octets()))
    else:
        return ''
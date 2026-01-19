def get_binary(self):
    """
        Si la dirección IP es válida, devuelve la forma binaria de la dirección IP; de lo contrario, devuelve ''
        :return: cadena
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
    if self.is_valid():
        return '.'.join((format(int(octet), '08b') for octet in self.ip_address.split('.')))
    else:
        return ''
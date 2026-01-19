def get_binary(self):
    """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
    if self.is_valid():
        return '.'.join((format(int(octet), '08b') for octet in self.get_octets()))
    else:
        return ''
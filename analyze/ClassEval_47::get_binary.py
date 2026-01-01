def get_binary(self):
    """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
    if not self.is_valid():
        return ''
    octets = self.get_octets()
    binary_octets = []
    for octet in octets:
        binary = bin(int(octet))[2:]
        binary_octets.append(binary.zfill(8))
    return '.'.join(binary_octets)
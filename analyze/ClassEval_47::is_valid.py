class IPAddress: 
    def __init__(self, ip_address):
        """
        Initialize the IP address to the specified address
        :param ip_address:string
        """
        self.ip_address = ip_address

    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
        :return: list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ["10", "10", "10", "10"]
        """
        if self.is_valid():
            return self.ip_address.split('.')
        else:
            return []

    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
        if self.is_valid():
            binary_octets = []
            for octet in self.get_octets():
                binary_octets.append(format(int(octet), '08b'))
            return '.'.join(binary_octets)
        else:
            return ''
    
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
            if not octet.isdigit() or not (0 <= int(octet) <= 255):
                return False
        return True
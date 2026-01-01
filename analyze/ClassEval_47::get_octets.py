def get_octets(self):
    """
        Si la dirección IP es válida, se devuelve la lista de cuatro números decimales separados por "." que constituyen la dirección IP; de lo contrario, se devuelve una lista vacía.
        :return: list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ["10", "10", "10", "10"]
        """
    if self.is_valid():
        return self.ip_address.split('.')
    else:
        return []
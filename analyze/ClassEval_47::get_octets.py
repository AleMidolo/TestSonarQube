def get_octets(self):
    """
        Se l'indirizzo IP è valido, viene restituita la lista di quattro numeri decimali separati da "." che costituiscono l'indirizzo IP; altrimenti, viene restituita una lista vuota.
        :return: lista
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ["10", "10", "10", "10"]
        """
    if self.is_valid():
        return self.ip_address.split('.')
    else:
        return []
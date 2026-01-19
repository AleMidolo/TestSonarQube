def get_octets(self):
    """
    Se l'indirizzo IP è valido, viene restituita la lista di quattro numeri decimali separati da "." che costituiscono l'indirizzo IP; altrimenti, viene restituita una lista vuota.
    :return: lista
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_octets()
    ["10", "10", "10", "10"]
    """
    if hasattr(self, 'ip_address') and self.ip_address:
        octets = self.ip_address.split('.')
        if len(octets) == 4:
            # Validate that each octet is a valid number between 0 and 255
            try:
                for octet in octets:
                    num = int(octet)
                    if num < 0 or num > 255:
                        return []
                return octets
            except ValueError:
                return []
    return []
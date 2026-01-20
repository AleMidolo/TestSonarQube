def get_octets(self):
    """
    Si la dirección IP es válida, se devuelve la lista de cuatro números decimales separados por "." que constituyen la dirección IP; de lo contrario, se devuelve una lista vacía.
    :return: list
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_octets()
    ["10", "10", "10", "10"]
    """
    if hasattr(self, 'ip_address') and self.ip_address:
        parts = self.ip_address.split('.')
        
        # Validate that we have exactly 4 parts
        if len(parts) != 4:
            return []
        
        # Validate each octet
        for part in parts:
            try:
                num = int(part)
                # Check if the number is in valid range (0-255)
                if num < 0 or num > 255:
                    return []
                # Check for leading zeros (except for "0" itself)
                if len(part) > 1 and part[0] == '0':
                    return []
            except ValueError:
                return []
        
        return parts
    
    return []
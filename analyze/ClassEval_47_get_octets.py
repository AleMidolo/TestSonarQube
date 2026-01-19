def get_octets(self):
    """
    If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
    :return: list
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_octets()
    ["10", "10", "10", "10"]
    """
    if hasattr(self, 'ip_address') and self.ip_address:
        parts = self.ip_address.split('.')
        
        # Validate IP address
        if len(parts) != 4:
            return []
        
        for part in parts:
            # Check if part is a valid number
            if not part:
                return []
            
            # Check for leading zeros (except "0" itself)
            if len(part) > 1 and part[0] == '0':
                return []
            
            # Check if it's a valid integer
            try:
                num = int(part)
                if num < 0 or num > 255:
                    return []
            except ValueError:
                return []
        
        return parts
    
    return []
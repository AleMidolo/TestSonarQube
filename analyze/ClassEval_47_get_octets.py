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
            
            # Check if all characters are digits
            if not part.isdigit():
                return []
            
            # Check if number is in valid range (0-255)
            if int(part) > 255:
                return []
        
        return parts
    
    return []
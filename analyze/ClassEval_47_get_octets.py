def get_octets(self):
    """
    If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
    :return: list
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_octets()
    ["10", "10", "10", "10"]
    """
    if not hasattr(self, 'ip_address') or not self.ip_address:
        return []
    
    parts = self.ip_address.split('.')
    
    # Check if there are exactly 4 parts
    if len(parts) != 4:
        return []
    
    # Validate each octet
    for part in parts:
        # Check if part is not empty and contains only digits
        if not part or not part.isdigit():
            return []
        
        # Check if the octet value is in valid range (0-255)
        if int(part) < 0 or int(part) > 255:
            return []
        
        # Check for leading zeros (except for "0" itself)
        if len(part) > 1 and part[0] == '0':
            return []
    
    return parts
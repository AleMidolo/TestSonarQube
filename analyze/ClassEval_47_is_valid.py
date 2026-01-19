def is_valid(self):
    """
    Judge whether the IP address is valid, that is, whether the IP address is composed of four Decimal digits separated by '.'. Each digit is greater than or equal to 0 and less than or equal to 255
    :return: bool
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.is_valid()
    True
    """
    try:
        parts = self.ip_address.split('.')
        
        # Must have exactly 4 parts
        if len(parts) != 4:
            return False
        
        for part in parts:
            # Each part must not be empty
            if not part:
                return False
            
            # Each part must be a valid integer (no leading zeros except for '0' itself)
            if len(part) > 1 and part[0] == '0':
                return False
            
            # Convert to integer and check range
            num = int(part)
            if num < 0 or num > 255:
                return False
        
        return True
    except (ValueError, AttributeError):
        return False
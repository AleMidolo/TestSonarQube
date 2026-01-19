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
        
        if len(parts) != 4:
            return False
        
        for part in parts:
            if not part:
                return False
            
            if not part.isdigit():
                return False
            
            if part[0] == '0' and len(part) > 1:
                return False
            
            num = int(part)
            if num < 0 or num > 255:
                return False
        
        return True
    except:
        return False
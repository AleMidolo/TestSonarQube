def get_octets(self):
    """
    यदि IP पता मान्य है, तो IP पते का निर्माण करने वाले चार दशमलव संख्याओं की सूची जो "." द्वारा अलग की गई है, लौटाई जाती है; अन्यथा, एक खाली सूची लौटाई जाती है
    :return: सूची
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_octets()
    ["10", "10", "10", "10"]
    """
    # Check if the IP address is valid
    if hasattr(self, 'ip_address') and self.ip_address:
        parts = self.ip_address.split('.')
        
        # Validate that we have exactly 4 parts
        if len(parts) != 4:
            return []
        
        # Validate each octet
        for part in parts:
            try:
                # Check if it's a valid number
                num = int(part)
                # Check if it's in valid range (0-255)
                if num < 0 or num > 255:
                    return []
                # Check for leading zeros (except for "0" itself)
                if len(part) > 1 and part[0] == '0':
                    return []
            except ValueError:
                return []
        
        return parts
    
    return []
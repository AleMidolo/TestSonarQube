def get_binary(self):
    """
    如果IP地址有效，返回IP地址的二进制形式；否则，返回''
    :return: 字符串
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_binary()
    "00001010.00001010.00001010.00001010"
    """
    # Assuming self has an ip_address attribute that stores the IP string
    # and a method to validate the IP address
    
    # Check if IP address is valid
    if not hasattr(self, 'ip_address') or not self.ip_address:
        return ''
    
    try:
        # Split the IP address into octets
        octets = self.ip_address.split('.')
        
        # Validate IP address format
        if len(octets) != 4:
            return ''
        
        binary_octets = []
        for octet in octets:
            # Convert to integer and validate range
            num = int(octet)
            if num < 0 or num > 255:
                return ''
            
            # Convert to binary (remove '0b' prefix) and pad to 8 bits
            binary = bin(num)[2:].zfill(8)
            binary_octets.append(binary)
        
        # Join with dots
        return '.'.join(binary_octets)
    
    except (ValueError, AttributeError):
        return ''
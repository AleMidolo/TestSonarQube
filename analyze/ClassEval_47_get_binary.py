def get_binary(self):
    """
    If the IP address is valid, return the binary form of the IP address; otherwise, return ''
    :return: string
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_binary()
    "00001010.00001010.00001010.00001010"
    """
    # Check if the IP address is valid
    if not hasattr(self, 'ip') or not self.ip:
        return ''
    
    # Split the IP address into octets
    parts = self.ip.split('.')
    
    # Validate IP address format
    if len(parts) != 4:
        return ''
    
    try:
        binary_parts = []
        for part in parts:
            # Convert to integer and validate range
            num = int(part)
            if num < 0 or num > 255:
                return ''
            # Convert to binary (remove '0b' prefix) and pad to 8 bits
            binary_parts.append(format(num, '08b'))
        
        # Join with dots
        return '.'.join(binary_parts)
    except ValueError:
        return ''
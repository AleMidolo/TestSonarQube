def get_binary(self):
    """
    如果IP地址有效，返回IP地址的二进制形式；否则，返回''
    :return: 字符串
    >>> ipaddress = IPAddress("10.10.10.10")
    >>> ipaddress.get_binary()
    "00001010.00001010.00001010.00001010"
    """
    # First, validate the IP address
    if not hasattr(self, 'ip') or not self.ip:
        return ''
    
    # Split the IP address into octets
    parts = self.ip.split('.')
    
    # Validate IP format
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
            binary = bin(num)[2:].zfill(8)
            binary_parts.append(binary)
        
        # Join with dots
        return '.'.join(binary_parts)
    except ValueError:
        return ''